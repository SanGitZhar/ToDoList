from django.contrib import admin
from .models import ToDoItem, ToDoList


admin.site.register(ToDoList)
admin.site.register(ToDoItem)
