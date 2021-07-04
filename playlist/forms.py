from django import forms

from .models import videoUpload

class PostForm(forms.ModelForm):
    class Meta:
        model = videoUpload
        fields = ('Title', 'Thumbnail','Price', 'Description','Video')




