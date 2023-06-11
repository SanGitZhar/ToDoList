from django.urls import path 
from .views import *

urlpatterns = [
    path("",index ,name='index'),
    path('task/<int:pk>/detail/', task_detail, name='task_detail'),
    path('task_create/', task_create, name='task_create' ),
    path('task/<int:pk>/edit/', task_edit, name="task_edit"),
    path('task/<int:pk>/delete/',task_delete, name="task_delete")
]   