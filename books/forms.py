# -*- coding: utf-8 -*-
from django import forms
from books.models import MyUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ['username', 'password']




