from django.urls import path
from task.views import TaskCreateAPI, AlltasksAPI, TaskUpdateAPI, TaskDetailAPI, TaskDeleteAPI

urlpatterns = [path('tasks/create/', TaskCreateAPI.as_view(), name='tasks_create'),
               path('tasks/', AlltasksAPI.as_view(), name='all-tasks'),
               path('tasks/<int:id>/', TaskDetailAPI.as_view(), name='task-detail'),
               path('tasks/<int:id>/update/', TaskUpdateAPI.as_view(), name='task_update'),
               path('tasks/<int:id>/delete/', TaskDeleteAPI.as_view(), name='task_delete')
]