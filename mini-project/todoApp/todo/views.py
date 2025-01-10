from django.shortcuts import render,redirect
from .models import Todo
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi")

def Task_view(request):
    all_task = Todo.objects.all()
    return render(request,'task_list.html',{'task':all_task})

def add_task(request):
    if request.method=='POST':
        title = request.POST['title']
        Todo.objects.create(title=title)
        return redirect('task_list')
    return render(request,'addtask.html')