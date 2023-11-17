from django.contrib import admin
from django.urls import path

from consulting.views import IndexView, AboutView, ContactView, ServiceView

app_name = 'consulting'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('service/', ServiceView.as_view(), name='service'),
]
