from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^lesson/$", views.LessonSelectView.as_view()),
    url(r"^lessonapply/$", views.LessonApplyView.as_view()),

]
