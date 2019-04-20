from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from lesson.serializers import LessonSerializer
from .models import lesson_table


class LessonSelectView(GenericAPIView, ListModelMixin):
    """
    获取课程数据视图
    路由：

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

    def post(self, request):
        querydict = request.data

        lclass_id = querydict.getlist("cid")[0]

        select_lesson = lesson_table.objects.filter(lclass_id=lclass_id)
        serializer = LessonSerializer(select_lesson, many=True)

        return Response(serializer.data)

