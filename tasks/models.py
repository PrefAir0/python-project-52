from django.db import models
from django.contrib.auth.models import User
from statuses.models import Status
from django.utils.translation import gettext_lazy as _
from labels.models import Label


class Task(models.Model):

    labels = models.ManyToManyField(
            Label,
            blank=True,
            related_name='tasks',
            verbose_name=_('Метки')
        )

    name = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("Задача с таким именем уже существует.")
        }
    )
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='tasks',
        verbose_name=_('Статус')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks',
        verbose_name=_('Автор')
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='executed_tasks',
        verbose_name=_('Исполнитель')
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
        related_name='tasks',
        verbose_name=_('Метки')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
