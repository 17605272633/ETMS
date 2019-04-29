from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r"^depart/$", views.DepartmentView.as_view()),
    url(r"^profession/$", views.ProfessionView.as_view()),
    url(r"^class/$", views.ClassView.as_view()),
    url(r"^classshow/$", views.ClassShowView.as_view()),
    # url(r"^departmentcrate/$", views.DepartmentCreateView.as_view()),
    url(r"^professioncreate/$", views.ProfessionCreateView.as_view()),
    url(r"^classcreate/$", views.ClassCreateView.as_view()),

]


from rest_framework.routers import DefaultRouter
# 创建可以处理视图的路由器对象router
router = DefaultRouter()
# 向路由器中注册路由集，router会自动帮我们添加路由
router.register('depart', views.DepartmentViewSet)
# 将路由器中的所以路由信息追到到django的路由列表中
urlpatterns += router.urls
