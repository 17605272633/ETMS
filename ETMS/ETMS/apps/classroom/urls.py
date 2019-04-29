from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^classroom/$", views.ClassRoomView.as_view()),
    url(r'^classroom/(?P<pk>\d+)/$', views.ClassRoomView.as_view())
]