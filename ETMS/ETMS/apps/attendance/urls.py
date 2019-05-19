from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^attendance/$', views.AttendanceCreateView.as_view()),
    url(r'^user_attendance/$', views.AttendanceGetView.as_view()),
    url(r'^up_attendance/$', views.AttendanceUploadView.as_view()),
]
