from django.shortcuts import render
from wiki.models import Category, Page


def wiki(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html', context)


def category(request, categoryID):
    context = {}
    try:
        category = Category.objects.get(id=categoryID)
        context['category'] = category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass
    return render(request, 'wiki/category.html', context)