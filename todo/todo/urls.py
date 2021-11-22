from django.contrib import admin
from django.urls import path
from todolist.views import todo
from todolist.views import category
from todolist.views import todo_dark, category_dark
#from todolist.views import alltc
from todolist.views import redirect_view


urlpatterns = [
	path('', redirect_view),
	path('todo/', todo, name = "TodoList"),
	path('todo_dark/', todo_dark),
    #path('alltc/', alltc),
    path('category_dark/', category_dark),
	path('category/', category, name = "Category"),
    path('admin/', admin.site.urls),
]
