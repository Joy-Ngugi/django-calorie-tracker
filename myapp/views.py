from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm
from django.db.models import Sum


def home(request):
    
    foods = Food.objects.all()
    total_calories = sum(food.calories for food in foods)
    
    context = {'foods': foods, 'total_calories': total_calories}
    
    return render(request, 'home.html', context)

def food_list(request):
    foods = Food.objects.all() 
    context = {'foods': foods}  
    return render(request, 'food_list.html', context) 

def add_food(request):
    if request.method =='POST':
        name = request.POST['name']
        calories = request.POST['calories']
        Food.objects.create(name=name, calories=calories)
        return redirect('home')
    return render(request, 'add_food.html')


def delete_food(request, food_id):
    Food.objects.get(id=food_id).delete()
    return redirect('home')

def reset_calories(request):
    Food.objects.all().delete()
    return redirect('home')