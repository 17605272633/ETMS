from django.conf.urls import url
from rest_framework import routers

from . import views

urlpatterns = [
    url('^report/$', views.ReportShowView.as_view()),
    url('^reportadd/$', views.ReportAddView.as_view()),
]


