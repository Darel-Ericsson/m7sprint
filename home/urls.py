from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    # path("home/", views.home, name="home"),
    path('home/', views.task, name='task'),
    path('home/<typ>', views.task, name='task'),
    path('task/create/<int:id>', views.create, name='create'),
    path('task/detail/<int:id>', views.detail, name='detail'),
    path('task/edit/<int:id>', views.edit, name='edit'),
    path('task/delete/<int:id>', views.delete, name='delete'),
]
