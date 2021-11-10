from django.shortcuts import render, redirect #для отображения и редиректа берем необходимые классы
from django.http import HttpResponse
from .models import TodoList, Category #не забываем наши модели

def redirect_view(request):
	return redirect("/category") # редирект с главной на категории

def todo(request):
	todos = TodoList.objects.all() #запрашиваем все объекты todo через менеджер объектов
	categories = Category.objects.all() #так же получаем все Категории
	if request.method == "POST": #проверяем то что метод именно POST
		if "Add" in request.POST: #проверяем метод добавления todo
			title = request.POST["description"] #сам текст
			date = str(request.POST["date"]) #дата, до которой должно быть закончено дело
			category = request.POST["category_select"] #категория, которой может выбрать или создать пользователь.
			content = title + " -- " + date + " " + category # полный склеенный контент
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() # сохранение нашего дела
			return redirect("/todo") # перегрузка страницы (ну вот так у нас будет устроено очищение формы)
		if "Delete" in request.POST: #если пользователь собирается удалить одно дело
			checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
			for i in range(len(checkedlist)): #мне почему-то не нравится эта конструкция
				todo = TodoList.objects.filter(id=int(checkedlist[i]))
				todo.delete() #удаление дела
	return render(request, "todo.html", {"todos": todos, "categories": categories})

def category(request):
	categories = Category.objects.all()  #запрашиваем все объекты Категорий
	if request.method == "POST": #проверяем что это метод POST
		if "Add" in request.POST: #если собираемся добавить
			name = request.POST["name"] #имя нашей категории
			category = Category(name=name) #у нашей категории есть только имя
			category.save() # сохранение нашей категории
			return redirect("/category")
		if "Delete" in request.POST: # проверяем есть ли удаление
			check = request.POST.getlist('check') #немного изменил название массива в отличии от todo, что бы было меньше путаницы в коде
			for i in range(len(check)):
				try:
					сateg = Category.objects.filter(id=int(check[i]))
					сateg.delete()   #удаление категории
				except BaseException: # вне сомнения тут нужно нормально переписать обработку ошибок, но на первое время хватит и этого
					return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
	return render(request, "category.html", {"categories": categories})

'''def alltc(request):
	def todo(request):
		todos = TodoList.objects.all() #запрашиваем все объекты todo через менеджер объектов
		categories = Category.objects.all() #так же получаем все Категории
		if request.method == "POST": #проверяем то что метод именно POST
			if "Add" in request.POST: #проверяем метод добавления todo
				title = request.POST["description"] #сам текст
				date = str(request.POST["date"]) #дата, до которой должно быть закончено дело
				category = request.POST["category_select"] #категория, которой может выбрать или создать пользователь.
				content = title + " -- " + date + " " + category # полный склеенный контент
				Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
				Todo.save() # сохранение нашего дела
				return redirect("/alltc") # перегрузка страницы (ну вот так у нас будет устроено очищение формы)
			if "Delete" in request.POST: #если пользователь собирается удалить одно дело
				checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
				for i in range(len(checkedlist)): #мне почему-то не нравится эта конструкция
					todo = TodoList.objects.filter(id=int(checkedlist[i]))
					todo.delete() #удаление дела
		return render(request, "alltc.html", {"todos": todos, "categories": categories})

	def category(request):
		categories = Category.objects.all()
		if request.method == "POST": #проверяем что это метод POST
			if "Add" in request.POST: #если собираемся добавить
				name = request.POST["name"] #имя нашей категории
				category = Category(name=name) #у нашей категории есть только имя
				category.save() # сохранение нашей категории
			return redirect("/alltc")
			if "Delete" in request.POST: # проверяем есть ли удаление
				check = request.POST.getlist('check') #немного изменил название массива в отличии от todo, что бы было меньше путаницы в коде
				for i in range(len(check)):
					try:
						сateg = Category.objects.filter(id=int(check[i]))
						сateg.delete()   #удаление категории
					except BaseException: # вне сомнения тут нужно нормально переписать обработку ошибок, но на первое время хватит и этого
						return HttpResponse('<h1>Сначала удалите карточки с этими категориями)</h1>')
		return render(request, "alltc.html", {"categories": categories})


	context = {
		'todos': TodoList.objects.all(),
		'categories': Category.objects.all(),
	}
	return render(request, "alltc.html", context, )'''