from django import forms
from .models import Post    


class DateInput(forms.DateInput):
    input_type = 'date'


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['client', 'responsible', 'date', 'material']           
        widgets = {
            'date': DateInput()
        }