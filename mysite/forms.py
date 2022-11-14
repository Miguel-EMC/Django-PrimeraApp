from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title of tarea", max_length=200)
    description = forms.CharField(label="Description of tarea", widget=forms.Textarea)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label='Name of projet', max_length=200)