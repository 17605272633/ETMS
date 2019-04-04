from django.shortcuts import render


# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin
from .models import *
from .serializers import DepartmentSerializer, ProfessionSerializer, ClassSerializer
from rest_framework.response import Response


def index(request):
    """主页"""
    return render(request, "html/index.html")


class DepartmentSelectView(GenericAPIView, ListModelMixin):
    """
    获取系信息视图
    路由：/depart/
    """
    # 获取查询集的查询条件自拟
    queryset = department_table.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request):
        return self.list(request)


class ProfessionSelectView(GenericAPIView, ListModelMixin):
    """
    获取专业数据视图
    路由：/profession/

    查询字符串: pdepart = ? , ?为department_table的did
    """
    # 获取查询集的查询条件自拟
    # queryset = profession_table.objects.all()
    # serializer_class = ProfessionSerializer

    def post(self, request):
        querydict = request.data

        pdepart = (querydict.getlist("pdepart"))

        select_profession = profession_table.objects.filter(pdepart=pdepart[0])
        serializer = ProfessionSerializer(select_profession, many=True)

        return Response(serializer.data)


class ClassSelectView(GenericAPIView, ListModelMixin):
    """
        获取班级数据视图
        路由：/class/

        查询字符串: cprofession = ? , ?profession_table的pid
        """

    # 获取查询集的查询条件自拟
    # queryset = profession_table.objects.all()
    # serializer_class = ProfessionSerializer

    def post(self, request):
        querydict = request.data

        cprofession = (querydict.getlist("cprofession"))

        select_class = class_table.objects.filter(cprofession=cprofession[0])
        serializer = ClassSerializer(select_class, many=True)

        return Response(serializer.data)
