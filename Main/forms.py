from django import forms

from .models import message


class PostForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ('FullName', 'Email','Phone','Message')
