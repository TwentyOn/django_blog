from django import forms
from .models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'category', 'thumbnail', 'status')

    def __init__(self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class EditPost(NewPost):
    class Meta:
        model = Post
        fields = NewPost.Meta.fields + ('fixed',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['fixed'].widget.attrs.update({'class': 'form-check-input'})
