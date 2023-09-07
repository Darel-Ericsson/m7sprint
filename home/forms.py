from django.forms import ModelForm
from django import forms
from django.utils import timezone
from .models import Task, Priority
from datetime import date

class CreateTask(ModelForm):
    class Meta:
        model = Task
        exclude = ['status']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción y observaciones',
            'task_owner' : 'Asignar a:',
            'task_priority' : 'Prioridad:',
            'deadline' : 'Fecha límite',
            'status' : 'Estado',
            'task_tag' : 'Etiqueta',
        }
        widgets = {
            'title': forms.TextInput( attrs={'class':'form-control'}),
            'description': forms.Textarea( attrs={'class':'form-control'}),
            'task_owner': forms.Select( attrs={'class':'form-control'}),
            'task_priority' : forms.Select( attrs={'class':'form-control'}),
            'deadline': forms.DateInput( attrs={'class':'form-control', 'type': 'date' , 'value': f'{timezone.now().date()}'}),
            'task_tag': forms.Select( attrs={'class':'form-control'}),
        }

class EditTask(ModelForm):
    class Meta:
        model = Task
        exclude = ['task_owner']
        labels = {
            'title' : 'Título',
            'description' : 'Descripción y observaciones',
            'task_priority' : 'Prioridad:',
            'deadline' : 'Fecha límite',
            'status' : 'Estado',
            'task_tag' : 'Etiqueta',
        }
        widgets = {
            'title': forms.TextInput( attrs={'class':'form-control'}),
            'description': forms.Textarea( attrs={'class':'form-control'}),
            'task_priority' : forms.Select( attrs={'class':'form-control'}),
            'status': forms.Select( attrs={'class':'form-control'}),
            'deadline': forms.DateInput( attrs={'class':'form-control', 'type': 'date'}),
            'task_tag': forms.Select( attrs={'class':'form-control'}),
        }