from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from .models import Status

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses:index')
    success_message = _('Статус успешно создан')

class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses:index')
    success_message = _('Статус успешно изменен')

class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:index')

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, _('Статус успешно удален'))
            return response
        except ProtectedError:
            messages.error(request, _('Невозможно удалить статус'))
            return redirect('statuses:index')