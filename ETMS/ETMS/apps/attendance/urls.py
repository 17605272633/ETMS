from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^stu_attendance/$', views.StudentAttendancePostView.as_view()),
    url(r'^stu_attendance/(?P<student_id>\d+)/$', views.StudentAttendanceGetView.as_view()),
    url(r'^tea_attendance/$', views.TeacherAttendancePostView.as_view()),
    url(r'^tea_attendance/(?P<teacher_id>\d+)/$', views.TeacherAttendanceGetView.as_view()),
]
