from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('food_list/', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]