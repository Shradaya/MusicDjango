from django import forms
from django.contrib.auth import get_user_model

non_allowed_usernames = ['abc']
# check for unique email & username

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label='UserName', widget=forms.TextInput(attrs={'size': '50',"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'size': '50', "class": "form-control"}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-confirm-password"
            }
        )
    )
    text="Sign In"
    textinup="Sign Up"
    link = "/signin/"

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid username, please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username, please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'size': '50',
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'size': '50',
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    text="Sign Up"
    textinup="Sign In"

    link ="/signup/"
    # def clean(self):
    #     data = super().clean()
    #     username = data.get("username")
    #     password = data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username
