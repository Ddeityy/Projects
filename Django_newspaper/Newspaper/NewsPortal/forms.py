from dataclasses import field
from django import forms
from django.core.exceptions import ValidationError
from .models import *


class UserForm(forms.ModelForm):
    authorUser = forms.CharField(
        label='Name'
    )
    class Meta:
        model = Author
        fields = [
            'authorUser',
            'age'
        ]

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username", 
                  "first_name", 
                  "last_name", 
                  "email", 
                  "password1", 
                  "password2", )

class PostForm(forms.ModelForm):
    text = forms.CharField()
    postCategory = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        label='Categories',
        )
    
    class Meta:
        model = Post
        fields =  [
            'title',
            'text',
            'author',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data