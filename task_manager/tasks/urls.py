from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView, TaskDetailView

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/detail/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('', TaskListView.as_view(), name='task_list')
]
