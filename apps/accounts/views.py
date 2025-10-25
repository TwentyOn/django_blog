from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.urls import reverse_lazy, reverse

from .models import Profile
from .forms import CustomUserCreationForm, CustomLoginForm, ProfileUpdateForm, UserUpdateForm


# Create your views here.
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'profile_pk'


class ProfileEdit(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/profile_update.html'
    pk_url_kwarg = 'profile_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['user_form'] = UserUpdateForm(data=self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                return self.render_to_response(context)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'profile_pk': self.object.pk})


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
