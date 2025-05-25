from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "created_at",
            "updated_at",
        ]


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "is_completed"]

'''docker compose up --build

Normally, we don't want all tasks details for easy read, we just want some essentials, like above.
'''