from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^lesson/$", views.LessonSelectView.as_view()),

]
