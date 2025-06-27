from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Task

# API - Zwraca JSON
def task_list_json(request):
    status = request.GET.get('status')
    priority = request.GET.get('priority')

    tasks = Task.objects.all()
    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)

    tasks = tasks.order_by('-created_at')

    data = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'priority': task.priority,
            'created_at': task.created_at,
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)

# HTML widok z dodawaniem
def task_list(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            priority=request.POST.get('priority')
        )
        return redirect('/tasks/')

    tasks = Task.objects.order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

# Usuwanie zadania
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('/tasks/')
