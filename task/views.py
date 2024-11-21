from django.shortcuts import render, redirect
from task.models import Task
from task.forms import TaskForm
from django.contrib import messages
# Create your views here.

def tasklist(request):
    tasklist = Task.objects.all().order_by("is_completed", "-created_at")
    context = {
        "tasklist": tasklist
    }
    return render(request, "task/tasklist.html", context)

def complete_task(request, id):
    task = Task.objects.get(id = id)
    task.is_completed = True
    task.save()
    messages.success(request, "Task Completed Successfully")
    return redirect("/tasks/")


def addedit_task(request, id = None):
    if id:
        task = Task.objects.get(id = id)
        form = TaskForm(instance = task)
    else:
        form = TaskForm()

    if request.method == "POST":
        form = TaskForm(data = request.POST, instance = task) if id else TaskForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Edited Successfully")
            return redirect("/tasks/")
    context = {
        "form": form
    }
    return render(request, "task/addedit_task.html", context)


def delete_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    messages.success(request, "Deleted Successfully")
    return redirect("/tasks/")