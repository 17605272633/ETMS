from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from classroom.models import classroom_table
from classroom.serializers import ClassRoomSerializer


class ClassRoomView(APIView):

    def get(self, request):
        """查询所有"""
        try:
            classroom = classroom_table.objects.all()
        except:
            return Response({"error": "查询失败"})

        # 序列化
        classroom_serializer = ClassRoomSerializer(classroom, many=True)
        classroom_dict = classroom_serializer.data

        return Response(classroom_dict)

    def post(self, request):
        """创建"""
        # 获取请求参数
        classroom_info = request.data

        crid = classroom_info.getlist("crid")[0]
        crname = classroom_info.getlist("crname")[0]
        crsize = classroom_info.getlist("crsize")[0]
        crdevice = classroom_info.getlist("crdevice")[0]

        # 将获取的数据上在数据库创建
        classroom_table.objects.create(
            crid=crid,
            crname=crname,
            crsize=crsize,
            crdevice=crdevice
        )

        return Response({
            "crid": crid,
            "crname": crname,
            "crsize": crsize,
            "crdevice": crdevice
        })

    def put(self, request, pk):
        """修改"""
        try:
            classroom = classroom_table.objects.get(crid=pk)
        except:
            return Response({"error": "查询错误"})

        # 接收
        classroom_dict = request.data

        # 验证
        classroom_serilizer = ClassRoomSerializer(classroom, data=classroom_dict)
        if not classroom_serilizer.is_valid():
            return Response(classroom_serilizer.errors)

        # 保存  update
        classroom = classroom_serilizer.save()

        # 响应
        classroom_serilizer = ClassRoomSerializer(classroom)
        classroom_dict = classroom_serilizer.data
        return Response(classroom_dict, status=201)

    def patch(self, request, pk):
        """局部更新"""
        try:
            classroom = classroom_table.objects.get(crid=pk)
        except:
            return Response({"error": "查询错误"})

        # 接收
        classroom_dict = request.data

        # 验证
        classroom_serilizer = ClassRoomSerializer(classroom, data=classroom_dict, partial=True)
        if not classroom_serilizer.is_valid():
            return Response(classroom_serilizer.errors)

        print(classroom_serilizer)
        # 保存  update
        classroom = classroom_serilizer.save()

        # 响应
        classroom_serilizer = ClassRoomSerializer(classroom)
        classroom_dict = classroom_serilizer.data
        return Response(classroom_dict, status=201)

    def delete(self, request, pk):
        """删除"""
        try:
            classroom = classroom_table.objects.get(crid=pk)
        except:
            return Response({"error": "查询错误"})

        # 删除
        classroom.delete()

        # 响应
        return Response(status=204)
