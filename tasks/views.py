from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
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

# HTML widok z listą i dodawaniem
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            return HttpResponseBadRequest("Title is required")
        Task.objects.create(
            title=title,
            description=request.POST.get('description', ''),
            status=request.POST.get('status', 'todo'),
            priority=request.POST.get('priority', 'medium')
        )
        return redirect('task_list')

    tasks = Task.objects.order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

# Widok do edycji zadania


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.priority = request.POST.get('priority')
        task.save()
        return redirect('task_list')

    return render(request, 'edit_task.html', {'task': task})


# Usuwanie zadania
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
