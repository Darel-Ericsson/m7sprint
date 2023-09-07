from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=10, default='Nueva')

    def __str__(self) -> str:
        return self.type

    
class Priority(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='Pendiente')
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_tag = models.ForeignKey(Tag, default=1,on_delete=models.CASCADE)
    task_priority = models.ForeignKey(Priority, default=1,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} > {self.task_owner}'
