from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    email_address = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)