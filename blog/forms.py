from django import forms
from .models import Post, Comment
from django.conf import settings


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Имя'}))
    email_from = forms.EmailField(initial=settings.EMAIL_HOST_USER,
                                  widget=forms.TextInput(attrs={"class": "form-control mb-1"}))
    email_to = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'E-mail получателя'}))
    comment = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={"class": "form-control mb-1", 'placeholder': 'Комментарий'}))


class CommentPostForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Ваше имя'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'Ваш комментарий'}))

    class Meta:
        model = Comment
        fields = ['name', 'body']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, label='Введите запрос',
                            required=False,
                            widget=forms.TextInput(
                                attrs={"class": "form-control mb-1", 'placeholder': 'Ввод запроса...'})
                            )
