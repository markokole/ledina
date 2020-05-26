from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import izberi, izhod

urlpatterns = [
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    path('admin/', admin.site.urls),
    path('registration/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('izberi', izberi, name='izberi'),
    #path('izhod', TemplateView.as_view(template_name='izhod.html'), name='izhod'),
    path('izhod', izhod, name='izhod'),
]
