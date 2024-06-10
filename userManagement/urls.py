from django.urls import path
from . import views

urlpatterns = [

    path("create/", views.author_create, name="author_create"),
    path('store', views.author_store, name="author_store"),
    path('', views.author_list, name="author_list"),
    path('<author_id>/delete', views.author_delete, name='author_delete'),
    path('<author_id>/active', views.author_activate, name='author_active'),
    path('<author_id>/edit', views.author_edit, name='author_edit'),
    path('<author_id>/update', views.author_update, name='author_update'),
             ]