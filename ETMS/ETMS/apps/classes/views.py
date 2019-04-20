from django.shortcuts import render


# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin
from .models import *
from .serializers import DepartmentSerializer, ProfessionSerializer, ClassSerializer
from rest_framework.response import Response


class DepartmentSelectView(GenericAPIView, ListModelMixin):
    """
    获取系信息视图
    路由：classes/depart/

    返回json: [
              {
                "did": 1,
                "dname": "人文与艺术系"
              },
              ...
            ]

    """
    # 获取查询集
    queryset = department_table.objects.all()
    # 获取序列化器
    serializer_class = DepartmentSerializer

    def get(self, request):
        return self.list(request)


class ProfessionSelectView(GenericAPIView, ListModelMixin):
    """
    获取专业数据视图
    路由：classes/profession/

    请求参数: pdepart = ? , ?为department_table的did

    返回jsom: [
              {
                "pid": 30101,
                "pname": "法学",
                "pdepart": 1
              },
              ...
            ]

    """

    def post(self, request):
        # 获取请求参数
        querydict = request.data
        pdepart = querydict.getlist("pdepart")[0]

        # 获取查询集
        select_profession = profession_table.objects.filter(pdepart=pdepart)
        # 将数据序列化
        serializer = ProfessionSerializer(select_profession, many=True)

        # 返回序列化的数据
        return Response(serializer.data)


class ClassSelectView(GenericAPIView, ListModelMixin):
    """
    获取班级数据视图
    路由：classes/class/

    请求参数: cprofession = ? , ?profession_table的pid

    返回json: [
              {
                "cid": 1530501,
                "cname": "2015计算机科学与技术一班",
                "cprofession": 80901
              },
              ...
            ]

    """

    def post(self, request):
        # 获取请求参数
        querydict = request.data
        cprofession = querydict.getlist("cprofession")[0]

        # 获取查询集
        select_class = class_table.objects.filter(cprofession=cprofession)
        # 将数据序列化
        serializer = ClassSerializer(select_class, many=True)

        # 返回序列化的数据
        return Response(serializer.data)
