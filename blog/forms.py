from django import forms
from .models import Post, Comment
from django.conf import settings


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=30)
    email_from = forms.EmailField(initial=settings.EMAIL_HOST_USER)
    email_to = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)

class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
