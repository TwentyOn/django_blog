from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-1',
                                                                              'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-1',
                                                                             'placeholder': 'Фамилия'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control mb-1',
                                                                            'placeholder': 'Логин'}))
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Email'}),
                             error_messages=({'invalid': 'Некорректный email-адресс'}), )
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control mb-1',
                                                                                 'placeholder': 'Пароль'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control mb-1',
                                                                                 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Логин'})
    )
    password = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Пароль'})
    )
    remember_me = forms.BooleanField(required=False)


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1",
                                                                          'placeholder': 'E-mail'}))
    username = forms.CharField(required=True, label='Имя пользователя', max_length=100,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1",
                                                             'placeholder': 'Логин'}))

    class Meta:
        model = User
        fields = ['email', 'username']


class UpdateProfileForm(forms.ModelForm):
    biografy = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control mb-1",
                                                            'placeholder': 'E-mail', 'rows': 5}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control mb-1",
                                                            'placeholder': 'E-mail'}))

    class Meta:
        model = Profile
        fields = ['biografy', 'avatar']
