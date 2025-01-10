from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('addtask/',views.add_task,name='addtask'),
    path('tasklist/',views.Task_view,name='task_list')
]