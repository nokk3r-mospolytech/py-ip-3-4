from .models import Region
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Region
        fields = ["regionName"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите регион'
            })
        }
