from django.urls import path
from .views import task_list, task_create, task_update, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('new/', task_create, name='task_create'),
    path('<int:pk>/edit/', task_update, name='task_update'),
    path('<int:pk>/delete/', task_delete, name='task_delete'),
]
