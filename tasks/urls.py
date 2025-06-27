from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # /tasks/
    path('json/', views.task_list_json, name='task_list_json'),  # /tasks/json/
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # /tasks/delete/1/
]
