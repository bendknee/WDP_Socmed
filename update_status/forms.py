from django import forms

class Status_Form(forms.Form):
    attrs = {
        'type': 'text',
        'class': 'todo-form-input',
        'placeholder':'What are you thinking today?',
    }
    title = forms.CharField(label='', required=True, max_length=140, widget=forms.TextInput(attrs=attrs))
