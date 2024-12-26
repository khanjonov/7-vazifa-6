from django.shortcuts import render, get_object_or_404
from .models import Flower, Category

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})


def flowers_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    flowers = Flower.objects.filter(category=category)
    return render(request, 'flowers/flowers_by_category.html', {'category': category, 'flowers': flowers})


def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})
