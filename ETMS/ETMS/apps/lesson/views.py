from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.serializers import LessonSerializer
from .models import lesson_table


class LessonSelectView(GenericAPIView):
    """
    获取课程数据视图
    路由：/lesson/lesson/

    """
    def get(self, request):
        """查询所有"""
        try:
            lesson = lesson_table.objects.all()
        except:
            return Response({"error": "查询失败"})

        # 序列化
        lesson_serializer = LessonSerializer(lesson, many=True)
        lesson_dict = lesson_serializer.data

        return Response(lesson_dict)

    def post(self, request):
        """

        请求参数: lclass_id = ? , ? class_table的cid

        返回json: [
              {
                "lid": 809010001,
                "lname": "C语言程序设计01",
                "ltime": 12,
                "lstart": "2018-09-10T22:58:03+08:00",
                "lend": "2018-12-10T22:58:20+08:00",
                "lclass": 1530501,
                "lteacher": 80901001
              },
              ...
            ]
        """
        querydict = request.data

        lclass_id = querydict.getlist("lclass_id")[0]

        select_lesson = lesson_table.objects.filter(lclass_id=lclass_id)
        serializer = LessonSerializer(select_lesson, many=True)

        return Response(serializer.data)


class LessonApplyView(APIView):
    """
    实验课程安排视图
    路由：/lesson/lessonapply/

    请求参数:


    """
    def post(self, request):
        """创建实验课程"""
        # 获取请求参数
        lesson_apply_info = request.data

        lid = lesson_apply_info.getlist("lid")[0]
        lname = lesson_apply_info.getlist("lname")[0]
        ltime = lesson_apply_info.getlist("ltime")[0]
        # lstart = lesson_apply_info.getlist("lstart")[0]
        lclass_id = lesson_apply_info.getlist("lclass_id")[0]
        lclassroom_id = lesson_apply_info.getlist("lclassroom_id")[0]
        lteacher_id = lesson_apply_info.getlist("lteacher_id")[0]

        # 将获取的数据上在数据库创建
        lesson_table.objects.create(
            lid=lid,
            lname=lname,
            ltime=ltime,
            lclass_id=lclass_id,
            lclassroom_id=lclassroom_id,
            lteacher_id=lteacher_id,
        )

        return Response({
            "lid": lid,
            "lname": lname,
            "ltime": ltime,
            "lclass_id": lclass_id,
            "lclassroom_id": lclassroom_id,
            "lteacher_id": lteacher_id,
        })



