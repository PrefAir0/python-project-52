from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('create/', views.UserCreateView.as_view(), name='create'),
]