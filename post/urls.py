from django.urls import path
from . import views

urlpatterns = [

    path("category/create/", views.category_create, name="category_create"),
    path('category/store', views.category_store, name="category_store"),
    # path('category/', views.category_list, name="category_list"),
    # path('<category_id>/delete', views.category_delete, name='category_delete'),
    # path('<category_id>/edit', views.category_edit, name='category_edit'),
    # path('<category_id>>/update', views.category_update, name='category_update'),
]
