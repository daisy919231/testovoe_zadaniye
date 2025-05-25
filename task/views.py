from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from task.serializers import TaskSerializer, AllTasksSerializer
from task.models import Task


# Create your views here.
class TaskCreateAPI(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AlltasksAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = AllTasksSerializer


class TaskDetailAPI(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"


class TaskUpdateAPI(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"


class TaskDeleteAPI(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"
