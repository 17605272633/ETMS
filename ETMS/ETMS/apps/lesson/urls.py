from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^lesson/$", views.LessonSelectView.as_view()),
    url(r"^lessonapply/$", views.LessonApplyView.as_view()),
    url(r"^teacher/$", views.TeacherLessonView.as_view()),
    url(r"^student/$", views.StudentLessonView.as_view()),

]
