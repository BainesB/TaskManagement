from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(title=title, description=description)
        return redirect("home")
    return render(request, "tasks/add_task.html")

def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'completed'
    task.save()
    return redirect('home')

def mark_pending(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'pending'
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
