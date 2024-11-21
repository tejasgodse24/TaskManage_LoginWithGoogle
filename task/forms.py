from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["is_completed"]

    def __init__(self, *args, **kwargs) -> None:
        super(TaskForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input_form flex-grow-1'
        
        