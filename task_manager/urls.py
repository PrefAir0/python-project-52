from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import UserLoginView, UserLogoutView
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'), 
]