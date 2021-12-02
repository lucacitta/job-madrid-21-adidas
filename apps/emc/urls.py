from django.urls import path

from .api.api import emc

urlpatterns = [
    path('',emc, name='emc'),
]