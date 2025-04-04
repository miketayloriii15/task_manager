from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    task_list = Task.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'task_list': task_list})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        Task.objects.create(name=name, priority=priority)
        return redirect('home')
    return render(request, 'myapp/add.html')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.name = request.POST.get('name', task.name)
        task.priority = request.POST.get('priority', task.priority)
        task.save()
        return redirect('home')
    return render(request, 'myapp/update.html', {'task': task})


