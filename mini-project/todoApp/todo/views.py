from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi")

def Task_view(request):
    all_task = Todo.objects.all()
    return render(request, 'task_list.html', {'task': all_task})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Get the title from the form
        if title:  # Ensure the title is not empty
            Todo.objects.create(title=title)  # Add the task to the database
    # Fetch the updated task list after adding
    all_task = Todo.objects.all()
    return render(request, 'addtask.html', {'task': all_task})


def Completed_task(request, task_id):
    
    task = get_object_or_404(Todo, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')  

def Delete_task(request, task_id):
    
    task = get_object_or_404(Todo, id=task_id)
    task.delete()
    return redirect('task_list')  
