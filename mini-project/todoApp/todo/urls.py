from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_task,name='addtask'),
    path('tasklist/',views.Task_view,name='task_list'),
    path('delete/<int:task_id>/',views.Delete_task,name='delete_task'),
    path('complete/<int:task_id>/',views.Completed_task,name='complete_task'),

]