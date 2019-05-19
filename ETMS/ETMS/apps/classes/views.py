from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import DepartmentSerializer, ProfessionSerializer, ClassSerializer, ClassShowSerializer
from rest_framework.response import Response


class DepartmentView(APIView):
    """
    系信息视图
    """

    def post(self, request):
        """
        创建系
        路由：POST classes/depart/

        返回json: {"message": "ok"}
        """

        # 获取请求参数
        querydict = request.data
        depart_name = querydict.getlist("class_name")[0]

        department_table.objects.create(
            dname=depart_name
        )

        return Response({"message": "ok"})

    def delete(self, request):
        """
        创建系
        路由：DELETE classes/depart/

        返回json: {"message": "ok"}
        """

        # 获取请求参数
        querydict = request.data
        depart_name = querydict.getlist("class_name")[0]

        department = department_table.objects.get(dname=depart_name)
        department.delete()

        return Response({"message": "ok"})


class ProfessionView(GenericAPIView):
    """
    获取专业数据视图
    路由：http://www.etms.mp:8000/classes/profess/

    """

    def get(self, request):
        profess = profession_table.objects.filter()
        profess_info = ProfessionSerializer(profess, many=True)

        return Response(profess_info.data)

    def post(self, request):
        """
        创建专业

        请求参数: pid = ? , pname = ? , pdepart_name = ?

        """
        # 获取请求参数
        querydict = request.data
        pid = querydict.getlist("pid")[0]
        pname = querydict.getlist("pname")[0]
        pdepart_name = querydict.getlist("pdepart_name")[0]

        # 获取专业对应系id
        # 按照班级id获取课程数据
        depart_querydict = department_table.objects.filter(dname=pdepart_name)
        depart_info = DepartmentSerializer(depart_querydict, many=True).data

        pdepart_id = depart_info[0]["id"]

        profession_table.objects.create(
            pid=pid,
            pname=pname,
            pdepart_id=pdepart_id
        )

        # 返回序列化的数据
        return Response({"message": "ok"})

    def delete(self, request):
        """删除"""
        # 获取请求参数
        querydict = request.data
        pid = querydict.getlist("pid")[0]

        try:
            profession_info = profession_table.objects.get(pid=pid)
        except:
            return Response({"error": "查询错误"})

        # 删除
        profession_info.delete()

        # 响应
        return Response(status=204)


class ClassView(GenericAPIView, ListModelMixin):
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

    def delete(self, request):
        """删除"""
        # 获取请求参数
        querydict = request.data
        cid = querydict.getlist("pid")[0]

        try:
            class_info = class_table.objects.get(cid=cid)
        except:
            return Response({"error": "查询错误"})

        # 删除
        class_info.delete()

        # 响应
        return Response(status=204)


class ClassShowView(GenericAPIView):
    """
    系,班级管理视图
    路由：classes/classshow/

    返回json:[
                {
                    "pid": 80901,
                    "pname":"计算机科学与技术",
                    "pclass":[
                                {
                                    "cid":1530501,
                                    "cname":"2015计算机科学与技术一班",
                                    "ccount": 30
                                },
                                ......
                            ]
                },
                ......
            ]
    """

    def get(self, request):
        # 获取系查询集
        queryset = profession_table.objects.all()
        # 获取系序列化器
        serializer_class = ProfessionSerializer
        # 将数据序列化
        profession_serializer = serializer_class(queryset, many=True)
        # 获取系的序列化数据
        profession_data = profession_serializer.data

        profession_list = []

        for profession in profession_data:
            profession_dict = {}

            pid = profession["pid"]
            pname = profession["pname"]

            pclass = class_table.objects.filter(cprofession_id=pid)

            profession_dict["pid"] = pid
            profession_dict["pname"] = pname
            profession_dict["pclass"] = pclass
            print(pclass)

            serializer = ClassShowSerializer(profession_dict)

            profession_list.append(serializer.data)

        return Response(profession_list)


class ProfessionCreateView(GenericAPIView):
    """
    专业创建视图
    路由：classes/professioncreate/

    请求参数: profession_id   专业id
             profession_name   专业名
             profession_depart   专业对应系
    """

    def post(self, request):
        querydict = request.data
        profession_id = querydict.getlist("profession_id")[0]
        profession_name = querydict.getlist("profession_name")[0]
        profession_depart = querydict.getlist("profession_depart")[0]

        # 将获取的数据上在数据库创建
        profession_table.objects.create(
            pid=profession_id,
            pname=profession_name,
            pdepart_id=profession_depart

        )
        return Response({
            "pid": profession_id,
            "pname": profession_name,
            "pdepart_id": profession_depart
        })


class ClassCreateDeleteView(GenericAPIView):
    """班级创建/删除视图"""

    def post(self, request):
        """
        班级创建视图
        路由：POST classes/classcreatedelete/

        请求参数: class_id   班号
                 class_name   班名
                 class_count   人数
                 profess_name  班级对应专业

        """

        querydict = request.data
        class_id = querydict.getlist("class_id")[0]
        class_name = querydict.getlist("class_name")[0]
        class_count = querydict.getlist("class_count")[0]
        profess_name = querydict.getlist("profess_name")[0]

        # 根据专业名获取专业号
        profess = profession_table.objects.filter(pname=profess_name)
        profess_data = ProfessionSerializer(profess, many=True)

        profess_id = profess_data.data[0]["pid"]

        # 将获取的数据上在数据库创建
        class_table.objects.create(
            cid=class_id,
            cname=class_name,
            ccount=class_count,
            cprofession_id=profess_id

        )
        return Response({"message": "ok"})

    def delete(self, request):
        """
        班级删除视图

        路由: DELETE /classes/classcreatedelete/
        """
        querydict = request.data
        class_id = querydict.getlist("class_id")[0]

        try:
            class_info = class_table.objects.get(cid=class_id)
        except:
            return Response({"error": "查询错误"})

        # 删除
        class_info.delete()

        # 响应
        return Response(status=204)
