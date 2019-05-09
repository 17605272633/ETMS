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

        # 获取请求数据
        querydict = request.data

        lclass_id = querydict.getlist("lclass_id")[0]

        # 按照班级id获取课程数据
        condition_lesson = lesson_table.objects.filter(lclass_id=lclass_id)
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
            "lid": lid,
            "lname": lname,
            "ltime": ltime,
            "lclass_id": lclass_id,
            "lclassroom_id": lclassroom_id,
            "lteacher_id": lteacher_id,
        })


class TeacherLessonView(APIView):
    """教师课表查询"""

    def post(self, request):
        """
        请求参数: lteacher_id = ?
        """

        # 获取请求数据
        querydict = request.data

        # 获取请求数据中的 教师id
        lteacher_id = querydict.getlist("lteacher_id")[0]

        # 在课程表中查询该教师的课数据,并序列化
        teacher_lesson = lesson_table.objects.filter(lteacher_id=lteacher_id)
        teacher_serializer = LessonSerializer(teacher_lesson, many=True)

        # 返回教师课表数据
        return Response(teacher_serializer.data)


class StudentLessonView(APIView):
    """学生课表查询"""

    def post(self, request):
        """
        请求参数: lstudent_id = ?
        """

        # 获取请求数据
        querydict = request.data

        # 获取请求数据中的 学生id
        lstudent_id = querydict.getlist("lstudent_id")[0]

        # 在 学生表 中按 学生id 查询该学生数据,并序列化
        student_queryset = student_table.objects.filter(sid=lstudent_id)
        student_serializer = StudentSerializer(student_queryset, many=True)

        # 获取序列化后的该学生数据
        student_data = student_serializer.data

        # 从数据中获取该学生所在 班级id
        student_info = student_data[0]
        lclass_id = student_info["sclass"]

        # 在 课程表 中按照 班级id 查询,并序列化
        student_lesson = lesson_table.objects.filter(lclass_id=lclass_id)
        student_serializer = LessonSerializer(student_lesson, many=True)

        # 返回学生课程表数据
        return Response(student_serializer.data)
