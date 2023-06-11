from django import forms
from .models import ToDoItem


class PostForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('task_title','description','todo_list',)





