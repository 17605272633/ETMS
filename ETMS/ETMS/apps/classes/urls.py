from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^depart/$", views.DepartmentView.as_view()),
    url(r"^profess/$", views.ProfessionView.as_view()),
    url(r"^class/$", views.ClassView.as_view()),
    url(r"^classshow/$", views.ClassShowView.as_view()),
    # url(r"^departmentcrate/$", views.DepartmentCreateView.as_view()),
    url(r"^professioncreate/$", views.ProfessionCreateView.as_view()),
    url(r"^classcreatedelete/$", views.ClassCreateDeleteView.as_view()),

]

