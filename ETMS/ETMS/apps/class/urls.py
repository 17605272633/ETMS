from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index),

    url(r"^depart/$", views.DepartmentSelectView.as_view()),
    url(r"^profession/$", views.ProfessionSelectView.as_view()),
    url(r"^class/$", views.ClassSelectView.as_view()),
]


