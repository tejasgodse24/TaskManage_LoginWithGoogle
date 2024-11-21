
from django.urls import path
from task.views import *

urlpatterns = [
    path('', tasklist, name="tasklist"),
    path('add/', addedit_task, name="add_task"),
    path('edit/<int:id>', addedit_task, name="edit_task"),
    path('delete/<int:id>', delete_task, name="delete_task"),
    path('complete/<int:id>', complete_task, name="complete_task"),

]
