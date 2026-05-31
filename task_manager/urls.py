from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from users.views import UserLoginView, UserLogoutView
from . import views 


def test_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-error/', test_error),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    path('', views.IndexView.as_view(), name='home'),
]