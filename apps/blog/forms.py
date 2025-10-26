from django import forms
from .models import Post, Comment


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'category', 'thumbnail', 'status')

    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class AddCommentPostForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('body',)


class EditPost(NewPost):
    class Meta:
        model = Post
        fields = NewPost.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fixed'].widget.attrs.update({'class': 'form-check-input'})
