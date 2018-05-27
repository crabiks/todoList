from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category

def index(request):
    return render(request, 'index.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {
        'categories' : categories
     })
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category = Category(
                name=name,
                color=color
            )
            category.save()
    return render(request, 'add_category.html')

def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category.name = name
            category.color = color
            category.save()
    return render(request, 'edit_category.html', {
        'category': category
    })
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories-list')
