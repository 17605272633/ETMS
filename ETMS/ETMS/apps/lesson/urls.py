from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^lesson/$", views.LessonSelectView.as_view()),
    url(r"^lessonadd/$", views.LessonApplyView.as_view()),
    url(r"^lessonall/$", views.AllLessonView.as_view()),


]
