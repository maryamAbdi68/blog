from django.shortcuts import render, redirect, get_object_or_404
from .models import Author

# Create your views here.


def author_create(request):
    return render(request, "userManagement/create.html")


def author_store(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        errors = author_validation(request.POST,"create" )

        if errors:
            return render(request, "userManagement/create.html", {'errors': errors})

        Author.objects.create(first_name=first_name, last_name=last_name, age=age)
        return redirect("author_list")

    return redirect("author_create")



def author_list(request):

    authors = Author.objects.all()
    return render(request, "userManagement/index.html", {'authors':authors})


def author_edit(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, "userManagement/edit.html", {'author': author})


def author_update(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST" and request.POST.get('_method') == 'PUT':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        errors = author_validation(request.POST,'updaate',author_id)
        if errors:
            return render(request, "userManagement/create.html", {'errors': errors})

        author.first_name = first_name
        author.last_name = last_name
        author.age = age
        author.save()
        return redirect("author_list")

    return redirect("author_create")

def author_validation(data,action,author_id=None):
    errors = {}
    if not data['age']:
        errors['age'] = 'age is required'
    if not data['first_name']:
        errors['first_name'] = 'firstname is required'
    else:
        if action == 'update':
            if Author.objects.filter(first_name=data['first_name']).exclude(pk=author_id).exists():
                errors['first_name'] = 'firstname is duplacated'
            else:
                if Author.objects.filter(first_name=data['first_name']).exists():
                    errors['first_name'] = 'firstname is duplacated'

def author_delete(request, author_id):
    author = get_object_or_404(Author,pk=author_id)
    if request.method == "POST" and request.POST.get('_method') == 'DELETE':
        author.delete()
    return redirect('author_list')


def author_activate(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if author.is_active:
        author.is_active = False
    else:
        author.is_active = True
    author.save()
    return redirect('author_list')