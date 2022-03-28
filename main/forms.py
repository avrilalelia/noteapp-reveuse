from django import forms
from django.db.models.fields import CharField


class CreateNewList(forms.Form):
    title = forms.CharField(label="List Title", max_length=200)


class CreateNewContent(forms.Form):
    text = forms.CharField(label="Note Text", max_length=10000,
                           widget=forms.Textarea())
    tag = forms.CharField(label="Tags", max_length=100)


class Register(forms.Form):
    username = forms.CharField(label="Username", max_length=200)
    password = forms.CharField(
        widget=forms.PasswordInput, label="Password",  max_length=200)
    email = forms.EmailField(label="Email",  max_length=200)


class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=200)
    password = forms.CharField(
        widget=forms.PasswordInput, label="Password",  max_length=200)
