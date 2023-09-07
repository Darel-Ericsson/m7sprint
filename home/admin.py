from django.contrib import admin
from .models import Task, Tag, Priority

# Register your models here.
admin.site.register(Tag)
admin.site.register(Priority)
admin.site.register(Task)
