from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('json/', views.task_list_json, name='task_list_json'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
