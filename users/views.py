from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView, DeleteView


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login') 
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


class UserPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):

        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, _('У вас нет прав для изменения'))
        return redirect('users:index')


class UserUpdateView(UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:index')
    success_message = _('Пользователь успешно изменен')


class UserDeleteView(UserPermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')

    def post(self, request, *args, **kwargs):
        messages.success(request, _('Пользователь успешно удален'))
        return super().post(request, *args, **kwargs)
