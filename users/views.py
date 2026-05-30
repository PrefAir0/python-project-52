from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:index')
    success_message = _('Пользователь успешно зарегистрирован')

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('home')
    success_message = _('Вы залогинены')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Вы разлогинены'))
        return super().dispatch(request, *args, **kwargs)