"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from tasks.views import register, user_login, dashboard, task_list, add_task, complete_task, edit_task, delete_task, user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/complete/<int:task_id>/', complete_task, name='complete_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('logout/', user_logout, name='logout'),
]