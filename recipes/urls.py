from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='home'), # An empty string '' means the homepage
    path('my_recipes/',views.user_recipes,name='my_recipes'),
    path('recipe_create/',views.recipe_create,name='recipe_create'),
    path('recipe/<int:pk>/',views.recipe_detail,name='recipe_detail')
]