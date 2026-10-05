from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    path('categories/', views.categories, name="categories"),
    path('categories/add', views.add_category, name="add_category"),
    path('categories/edit/<int:pk>/', views.edit_category, name="edit_category"),
    path('categories/delete/<int:pk>/', views.delete_category, name="delete_category"),

    path('blogs/', views.blogs, name="blogs"),
    path('blogs/add', views.add_blogs, name='add_blogs'),
    path('blogs/edit/<int:pk>/', views.edit_blogs, name="edit_blogs"),
    path('blogs/delete/<int:pk>/', views.delete_blogs, name="delete_blogs"),

    path('users/', views.users, name="users"),
    path('users/add/', views.add_user, name="add_user"),
    path('users/edit/<int:pk>/', views.edit_user, name="edit_user"),
    path('users/delete/<int:pk>/', views.delete_user, name="delete_user"),

    path('newsletter/', views.newsletter, name="newsletter"),
    path('newsletter/add', views.add_newsletter, name="add_newsletter"),
    path('newsletter/edit/<int:pk>/', views.edit_newsletter, name="edit_newsletter"),
    path('newsletter/delete/<int:pk>/', views.delete_newsletter, name="delete_newsletter")
]