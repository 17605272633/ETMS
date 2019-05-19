from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from lesson.serializers import LessonSerializer
from users.models import student_table
from users.serializers import StudentSerializer
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

        # 返回
        return Response(lesson_dict)

    def post(self, request):
        """
        按条件获取课程数据
        请求参数: user_id = ? , userkind = ?

        返回json: [
              {
                "lid": 809010001,
                "lname": "C语言程序设计01",
                "ltime": 12,
                "lclass_id": 1530501,
                "lclassroom_id": 101,
                "lteacher_id": 80901001
              },
              ...
            ]
        """

        # 获取请求数据
        querydict = request.data

        userkind = querydict.getlist("userkind")[0]
        user_id = querydict.getlist("user_id")[0]

        # 教师
        if userkind == "1":

            # 按照教师id获取课程数据
            condition_lesson = lesson_table.objects.filter(lteacher_id=user_id)
            condition_serializer = LessonSerializer(condition_lesson, many=True)

            return Response(condition_serializer.data)

        # 学生
        if userkind == "2":

            # 获取该学生班号
            stu_querydict = student_table.objects.filter(sid=user_id)
            stu_info = StudentSerializer(stu_querydict, many=True).data

            print(stu_info)

            class_id = stu_info[0]["sclass"]

            # 按照班级id获取课程数据
            condition_lesson = lesson_table.objects.filter(lclass_id=class_id)
            condition_serializer = LessonSerializer(condition_lesson, many=True)

            return Response(condition_serializer.data)



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
            "message": "ok"
        })


class AllLessonView(APIView):
    """课表查询"""

    def post(self, request):
        """
        路由 POST /lesson/lessonall/
        请求参数: lclass_id = ?
        """

        # 获取请求数据
        querydict = request.data

        # 获取请求数据中的 教师id
        lclass_id = querydict.getlist("lclass_id")[0]

        # 在课程表中查询该教师的课数据,并序列化
        class_lesson = lesson_table.objects.filter(lclass_id=lclass_id)
        lesson_serializer = LessonSerializer(class_lesson, many=True)

        # 返回教师课表数据
        return Response(lesson_serializer.data)


