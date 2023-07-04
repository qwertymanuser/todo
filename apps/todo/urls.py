from django.urls import path
from todo.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('api/v1/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/v1/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]