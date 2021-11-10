from django.contrib import admin
from django.urls import path
from todolist.views import todo
from todolist.views import category
#from todolist.views import alltc
from todolist.views import redirect_view


urlpatterns = [
	path('', redirect_view),
	path('todo/', todo, name = "TodoList"),
    #path('alltc/', alltc),
	path('category/', category, name = "Category"),
    path('admin/', admin.site.urls),
]
