from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Привет от Хекслета! Менеджер задач запущен.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]