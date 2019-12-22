"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from folders import views as folders_views
from pages import views as pages_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', folders_views.index, name='index'),
    path('folders/', folders_views.search, name='search_view'),
    path('folders/<int:pk>/', folders_views.page_show, name='page_show'),
    path('folders/<int:pk>/delete/', folders_views.folder_delete, name='folder_delete'),
    path('folders/<int:fpk>/pages/<int:pk>/delete/', folders_views.page_delete, name='page_delete'),
    path('folders/pages/<int:pk>/delete/', folders_views.search_delete, name='search_delete'),
    path('tags/<int:pk>/', folders_views.tag_show, name='tag_show'),
    path('tags/<int:tpk>/pages/<int:pk>/delete/', folders_views.tag_page_delete, name='tag_page_delete'),
    # path('test/', pages_views.page_show, name='page_show'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
