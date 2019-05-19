from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^user/$", views.UserManagementView.as_view()),
    url(r"^user/logout/$", views.UserLogOutView.as_view()),
    url(r"^super/$", views.SupermanagementView.as_view()),
    url(r"^super/(?P<userkind>\d+)/$", views.SupermanagementView.as_view()),
    url(r'^super/(?P<userkind>\d+)/(?P<id>\d+)/$', views.SupermanagementView.as_view()),
    url(r"^student/$", views.StudentView.as_view()),
    url(r"^studentfind/$", views.StudentFindView.as_view()),
    url(r"^teacher/$", views.TeacherView.as_view()),

]

