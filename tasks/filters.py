import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Task
from labels.models import Label

class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Метка')
    )
    
    self_tasks = django_filters.BooleanFilter(
        label=_('Только свои задачи'),
        widget=forms.CheckboxInput(),
        method='filter_self_tasks'
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset