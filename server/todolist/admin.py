from django.contrib import admin
from todolist.models import TodoList, Tags

admin.site.register(TodoList)
admin.site.register(Tags)