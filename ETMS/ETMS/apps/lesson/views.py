from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from lesson.serializers import LessonSerializer
from .models import lesson_table


class LessonSelectView(GenericAPIView, ListModelMixin):
    """
    获取课程数据视图
    路由：/lesson/lesson/

    查询字符串: lclass_id = ? , ? class_table的cid
    """

    def post(self, request):
        querydict = request.data

        lclass_id = (querydict.getlist("cid"))

        select_lesson = lesson_table.objects.filter(lclass_id=lclass_id[0])
        serializer = LessonSerializer(select_lesson, many=True)

        return Response(serializer.data)

