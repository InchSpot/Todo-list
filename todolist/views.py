from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import TodoList, Status, Priority
from . import forms
 
def redirect_view(request):
    return redirect("/todo") 

def todo(request):
    todos = TodoList.objects.all() #запрашиваем все объекты todo через менеджер объектов
    statuses = Status.objects.all()
    priorities = Priority.objects.all()
    status_form = forms.StatusForm()
    priority_form = forms.PriorityForm()
    if request.method == "POST": #проверяем то что метод именно POST
        if "Add" in request.POST: #проверяем метод добавления todo
            title = request.POST["description"] #сам текст
            date = str(request.POST["date"]) #дата, до которой должно быть закончено дело
            status_str = request.POST['status_select']
            status, created = Status.objects.get_or_create(name = status_str)
            priority_str = request.POST['priority_select']  
            priority, created = Priority.objects.get_or_create(name = priority_str)
            content = title + " -- " + date + " " + status_str + " " + priority_str  # полный склеенный контент
            Todo = TodoList(title=title, content=content, due_date=date, status=status, priority=priority )
            Todo.save() # сохранение нашего дела
            return redirect("/todo") # перегрузка страницы (ну вот так у нас будет устроено очищение формы)
        if "Delete" in request.POST: #если пользователь собирается удалить одно дело
            checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
            for i in range(len(checkedlist)): #мне почему-то не нравится эта конструкция
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete() #удаление дела
    return render(request, "todo.html", {"todos": todos, "statuses": status_form, "priorities": priority_form})