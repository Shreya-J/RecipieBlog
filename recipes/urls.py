from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='home'), # An empty string '' means the homepage
]