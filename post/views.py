from django.shortcuts import render, redirect, get_object_or_404
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


def category_edit(request, category_id):
    pass

def category_delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
        category.delete()

    return redirect('category_list')