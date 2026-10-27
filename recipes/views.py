from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm

# Create your views here.
def all_recipes(request):
    # Fetch EVERY recipe from the database
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'recipes/home.html', {'recipes': recipes})

@login_required
def user_recipes(request):
    # This is the "Magic" line:
    recipes = Recipe.objects.filter(created_by=request.user) 
    return render(request, 'recipes/my_recipes.html', {'recipes': recipes})


def recipe_detail(request, pk):
    # 'pk' stands for Primary Key (the ID)
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Commit=False lets us modify the object before saving it to the DB
            recipe = form.save(commit=False)
            recipe.created_by = request.user # This is the "Ownership" link
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})