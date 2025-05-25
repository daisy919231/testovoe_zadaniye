from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Task(BaseModel):
    title=models.CharField(max_length=100, null=True)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title