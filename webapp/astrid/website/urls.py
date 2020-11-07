from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('users/<int:user_id>', views.userPage, name='userPage'),
    path('feed/', views.feed, name ='feed'),
    path('fed/', views.fed, name='fed')
]