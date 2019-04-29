from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import DepartmentSerializer, ProfessionSerializer, ClassSerializer, ClassShowSerializer
from rest_framework.response import Response


class DepartmentViewSet(ModelViewSet):
    """
    获取全部系信息
    GET  /classes/depart/

    返回json: [
                  {
                    "did": 1,
                    "dname": "人文与艺术系"
                  },
                ...
            ]

    获取单个系信息
    GET  /classes/depart/<pk>/

    创建一个系信息
    POST  /classes/depart/

    修改某一个系信息
    PUT  /classes/depart/<pk>/

    删除某个系信息
    DELETE /classes/depart/<pk>/

    """

    queryset = department_table.objects.all()
    serializer_class = DepartmentSerializer


# class DepartmentView(GenericAPIView, ListModelMixin):
#     """
#     系信息视图
#     """
#     # 获取查询集
#     queryset = department_table.objects.all()
#     # 获取序列化器
#     serializer_class = DepartmentSerializer
#
#     def get(self, request):
#         """
#         获取系信息
#         路由：GET classes/depart/
#
#         返回json: [
#                   {
#                     "did": 1,
#                     "dname": "人文与艺术系"
#                   },
#                   ...
#                 ]
#         """
#         return self.list(request)


class ProfessionView(GenericAPIView):
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


# class DepartmentCreateView(GenericAPIView):
#     """
#     系创建视图
#     路由：classes/departmentcrate/
#
#     请求参数: depart_name   系名
#
#     """
#
#     def post(self, request):
#         querydict = request.data
#         depart_name = querydict.getlist("depart_name")[0]
#
#         # 将获取的数据上在数据库创建
#         department_table.objects.create(
#             dname=depart_name
#         )
#
#         return Response(depart_name)


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


class ClassCreateView(GenericAPIView):
    """
    班级创建视图
    路由：classes/classcreate/

    请求参数: class_id   班号
             class_name   班名
             ccount   人数
             class_profession  班级对应专业

    """

    def post(self, request):
        querydict = request.data
        class_id = querydict.getlist("class_id")[0]
        class_name = querydict.getlist("class_name")[0]
        class_profession = querydict.getlist("class_profession")[0]

        # 将获取的数据上在数据库创建
        class_table.objects.create(
            cid=class_id,
            cname=class_name,
            ccount=0,
            cprofession_id=class_profession

        )
        return Response({
            "cid": class_id,
            "cname": class_name,
            "ccount": 0,
            "cprofession_id": class_profession
        })
