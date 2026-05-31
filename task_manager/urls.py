from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import UserLoginView, UserLogoutView


def test_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
