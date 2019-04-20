from django.conf.urls import url
from rest_framework import routers

from . import views

urlpatterns = [
    url('^(?P<class_id>\d+)/report/$', views.ReportShowView.as_view()),
    url('^report/$', views.ReportAddView.as_view()),
]


