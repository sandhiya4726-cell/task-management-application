from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(request, 'tasks/login.html', {'form': form})
def dashboard(request):
    return render(request, 'tasks/dashboard.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')
@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_task.html', {'form': form})
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()

    return redirect('task_list')

def user_logout(request):
    logout(request)
    return redirect('login')