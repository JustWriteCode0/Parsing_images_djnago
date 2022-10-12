from django import forms
from .models import Url


# форма наследует поля из модели Url
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = '__all__'





