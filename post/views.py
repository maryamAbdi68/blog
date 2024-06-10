from django.shortcuts import render, redirect
from .models import Category


def category_create(request):
    return render(request, 'post/category/create.html')


def category_store(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        errors = category_validation(request.POST,'create')
        if errors:
            return render(request, 'post/category/create.html',{"errors":errors})

        Category.objects.create(title=title)
        return redirect("category_list")



def category_validation(data,action,category_id=None):

    errors = {}
    if not data['title']:
        errors['title'] = 'title is required'
    else:
        if action == 'create':
            if Category.objects.filter(title=data['title']).exists():
                errors['title'] = 'title is duplicated'
        else:
            if Category.objects.filter(title=data['title']).exclude(pk=category_id).exists():
                errors['title'] = 'title is duplicated'

    return errors