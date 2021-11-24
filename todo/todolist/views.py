from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import TodoList, Category 

def redirect_view(request):
	return redirect("/category") # редирект

def todo(request):
	todos = TodoList.objects.all() 
	categories = Category.objects.all() 
	if request.method == "POST": 
		if "Add" in request.POST: 
			title = request.POST["description"] #текст
			date = str(request.POST["date"]) #дата [закончить]
			category = request.POST["category_select"] #категория
			content = title + " -- " + date + " " + category # всё вместе
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() # сохранить
			return redirect("/todo") # перегрузка
		if "Delete" in request.POST: # если удалить
			checkedlist = request.POST.getlist('checkedbox') # список выделенных дел
			for i in range(len(checkedlist)):
				todo = TodoList.objects.filter(id=int(checkedlist[i]))
				todo.delete() #удаление
	return render(request, "todo.html", {"todos": todos, "categories": categories})

def category(request):
	categories = Category.objects.all()
	if request.method == "POST": 
		if "Add" in request.POST: #если добавить
			name = request.POST["name"] #имя 
			category = Category(name=name)
			category.save() # сохранение
			return redirect("/category")
		if "Delete" in request.POST: # проверяем удаление
			check = request.POST.getlist('check')
			for i in range(len(check)):
				try:
					сateg = Category.objects.filter(id=int(check[i]))
					сateg.delete()   #удаление кат
				except BaseException: # переписать!!!!!!
					return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
	return render(request, "category.html", {"categories": categories})


def todo_dark(request):
	todos = TodoList.objects.all() 
	categories = Category.objects.all() 
	if request.method == "POST": 
		if "Add" in request.POST: 
			title = request.POST["description"] #текст
			date = str(request.POST["date"]) #дата [закончить]
			category = request.POST["category_select"] #категория
			content = title + " -- " + date + " " + category # всё вместе
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() # сохранить
			return redirect("/todo") # перегрузка
		if "Delete" in request.POST: # если удалить
			checkedlist = request.POST.getlist('checkedbox') # список выделенных дел
			for i in range(len(checkedlist)):
				todo = TodoList.objects.filter(id=int(checkedlist[i]))
				todo.delete() #удаление
	return render(request, "todo_dark.html", {"todos": todos, "categories": categories})

def category_dark(request):
	categories = Category.objects.all()
	if request.method == "POST": 
		if "Add" in request.POST: #если добавить
			name = request.POST["name"] #имя 
			category = Category(name=name)
			category.save() # сохранение
			return redirect("/category")
		if "Delete" in request.POST: # проверяем удаление
			check = request.POST.getlist('check')
			for i in range(len(check)):
				try:
					сateg = Category.objects.filter(id=int(check[i]))
					сateg.delete()   #удаление кат
				except BaseException: # переписать!!!!!!
					return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
	return render(request, "category_dark.html", {"categories": categories})

