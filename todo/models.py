from django.db import models

class Task(models.Model):
    taskName = models.CharField(max_length=255)
    isCompleted = models.BooleanField(default=False)
    isEditable = models.BooleanField(default=False)