from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index),
    url(r"^lesson$", views.lesson),
    url(r"^classroom$", views.classroom),
    url(r"^classes$", views.classes),
    url(r"^attendance$", views.attendance),
    url(r"^super_student$", views.super_student),
    url(r"^super_teacher$", views.super_teacher),
]