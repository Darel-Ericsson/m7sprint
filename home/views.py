from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

from .forms import CreateTask, EditTask
from .models import Task, Tag
from user_manager.forms import CustomCreationForm

# Create your views here.
def home(request):
    context = {}
    return render(request, "home/home.html", context)

@login_required
def task(request, typ=None):
    formCreateTask = CreateTask()
    tags = Tag.objects.all() 

    tasks_pending = Task.objects.filter(task_owner=request.user, status='Pendiente')
    tasks_inprogress = Task.objects.filter(task_owner=request.user, status='En progreso')
    tasks_completed = Task.objects.filter(task_owner=request.user, status='Completada')
    tasks_expired = Task.objects.filter(task_owner=request.user, deadline__lt=timezone.now().date())
    tasks_filterTag = Task.objects.filter(task_owner=request.user, task_tag=typ)

    pending_tasks = tasks_pending.count()
    inprogress_tasks = tasks_inprogress.count()
    completed_tasks = tasks_completed.count()
    expired_tasks = tasks_expired.count()
    is_expired = False
    select_filter = request.GET.get('filter_option')

    if typ != None:
        is_expired = False
        tasks =  tasks_filterTag.order_by('deadline')
        title_list = f'buenos días'
        formCreateTask = CreateTask()
        return render(request, 'task/task.html', {
            'tasks' : tasks,
            'formCreateTask': formCreateTask,
            'title_list' : title_list,
            'is_expired' : is_expired,
            'pending_tasks' : pending_tasks,
            'inprogress_tasks' : inprogress_tasks,
            'completed_tasks' : completed_tasks,
            'expired_tasks' : expired_tasks,
            'tags': tags,
        })

    if select_filter == 'inprogress':
        tasks =  tasks_inprogress .order_by('deadline')
        title_list = 'estas son tus tareas en progreso.'
     
    elif select_filter == 'completed':
        tasks = tasks_completed.order_by('deadline')
        title_list = 'estas son tus tareas completadas'
        
    elif select_filter == 'expired':
        tasks = tasks_expired
        title_list = 'estas son tus tareas expiradas'
        is_expired = True
        
    else:
        tasks = tasks_pending.order_by('deadline')
        title_list = 'estas son tus tareas pendientes.'
        tasks_pending = tasks.count()
        
    
    
    return render(request, 'task/task.html', {
        'tasks' : tasks,
        'formCreateTask': formCreateTask,
        'title_list' : title_list,
        'is_expired' : is_expired,
        'pending_tasks' : pending_tasks, 
        'inprogress_tasks' : inprogress_tasks,
        'completed_tasks' : completed_tasks,
        'expired_tasks' : expired_tasks,
        'tags': tags, 
    })



@login_required
def create(request, id):
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            print(task.task_owner_id)
            if not request.user.is_superuser or task.task_owner_id == None:
                task.task_owner_id = id
            task.save()
            return redirect('home:task')
    return render(request, 'task/createTask.html', {
        'form': CreateTask()
    })

@login_required
def detail(request, id):
    taskDetail = get_object_or_404(Task, id=id)
    return render(request, 'task/detail.html', {
        'taskDetail': taskDetail
    })

@login_required
def edit(request, id):
    task =  get_object_or_404(Task, id=id)
    
    if request.method == 'POST':
        formEditTask = EditTask(request.POST, instance=task)
        if formEditTask.is_valid():
            formEditTask.save()
            return redirect('home:task')
        else:
            messages.error(request, 'Ha ocurrido un error, vuelva a intentarlo')
    else:
        formatted_deadline = task.deadline.strftime('%Y-%m-%d')
        formEditTask = EditTask(instance=task, initial={'deadline': formatted_deadline})

    return render(request, 'task/editTask.html', {
        "formEditTask": formEditTask
    })

@login_required
def delete(request, id):
    taskDelete = get_object_or_404(Task, id=id)
    taskDelete.delete()
    return redirect('home:task')