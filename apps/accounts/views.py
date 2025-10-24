from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User

from .models import Profile
from .forms import CustomUserCreationForm


# Create your views here.
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'


class CreateUser(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/login.html'
