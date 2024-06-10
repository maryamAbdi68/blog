from django.db import models
from userManagement.models import Author


class Category(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateField(auto_now=True)


class Tag(models.Model):
    caption = models.CharField(max_length=50)


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    create_at = models.DateField(auto_now=True)





