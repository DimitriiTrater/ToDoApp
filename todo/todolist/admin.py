from django.contrib import admin
from .models import TodoList, Category

admin.site.register(TodoList)
admin.site.register(Category)
