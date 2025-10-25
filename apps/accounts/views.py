from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Profile
from .forms import CustomUserCreationForm, CustomLoginForm


# Create your views here.
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'


class UserRegister(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context


class CustomLogin(SuccessMessageMixin, LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    next_page = 'post_list'
    success_message = 'Вы успешно авторизовались!'


class CustomLogout(SuccessMessageMixin, LogoutView):
    next_page = 'post_list'
    success_message = 'Успешный выход из системы.'
