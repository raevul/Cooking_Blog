from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='home'),
   path('category/<str:slug>/', category_detail, name='category'),
   path('recipe_detail/<int:pk>/', recipe_detail, name='recipe_detail'),
   path('add_recipe/', add_recipe, name='add_recipe'),
   path('update_recipe/<int:pk>/', update_recipe, name='update_recipe'),
   path('delete_recipe/<int:pk>/', delete_recipe, name='delete_recipe'),
]
