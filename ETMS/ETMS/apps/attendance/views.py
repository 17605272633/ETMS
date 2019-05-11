from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models import student_attendance_table, teacher_attendance_table
from attendance.serializers import StudentAttendanceSerializer, TeacherAttendanceSerializer
from lesson.models import lesson_table
from lesson.serializers import LessonSerializer


class StudentAttendanceGetView(GenericAPIView):
    """
    学生考勤管理  按学号查询
    """

    def get(self, request, student_id):
        """
        根据路由中班级id获取相关学生考勤

        路由: GET attendance/stu_attendance/(?P<student_id>\d+)/
        """
        try:
            stu_attendance = student_attendance_table.objects.filter(asuser_id=student_id)
        except:
            return Response({"error": "查询失败"})

        # 序列化
        stu_attendance_serializer = StudentAttendanceSerializer(stu_attendance, many=True)
        stu_attendance_dict = stu_attendance_serializer.data

        return Response(stu_attendance_dict)

    # def patch(self, request, student_id):
    #     """局部修改"""
    #     try:
    #         stu_attendance = student_attendance_table.objects.get(asuser_id=student_id)
    #     except:
    #         return Response({"error": "查询错误"})
    #
    #     # 接收
    #     stu_attendance_dict = request.data
    #
    #     # print(stu_attendance)
    #
    #     # 验证
    #     stu_attendance_serilizer = StudentAttendanceSerializer(stu_attendance, data=stu_attendance_dict, partial=True)
    #     if not stu_attendance_serilizer.is_valid():
    #         return Response(stu_attendance_serilizer.errors)
    #
    #     # 保存  update
    #     stu_attendance = stu_attendance_serilizer.save()
    #
    #     # 响应
    #     stu_attendance_serilizer = StudentAttendanceSerializer(stu_attendance)
    #     stu_attendance_dict = stu_attendance_serilizer.data
    #     return Response(stu_attendance_dict, status=201)

    def delete(self, request, student_id):
        """删除"""
        try:
            stu_attendance = student_attendance_table.objects.get(asuser_id=student_id)
        except:
            return Response({"error": "查询错误"})

        # 删除
        stu_attendance.delete()

        # 响应
        return Response(status=204)


class StudentAttendancePostView(GenericAPIView):
    """
    创建学生考勤信息
    路由: POST attendance/stu_attendance/
    """

    def post(self, request):
        """创建考勤信息"""
        # 获取请求参数
        stu_attendance = request.data

        # asid = stu_attendance.getlist("asid")[0]
        # astime = stu_attendance.getlist("astime")[0]
        asstatus = stu_attendance.getlist("asstatus")[0]
        alesson_id = stu_attendance.getlist("alesson_id")[0]
        asuser_id = stu_attendance.getlist("asuser_id")[0]

        # 将获取的数据上在数据库创建
        student_attendance_table.objects.create(
            # asid=asid,
            # astime=astime,
            asstatus=asstatus,
            alesson_id=alesson_id,
            asuser_id=asuser_id
        )

        return Response({
            # "asid": asid,
            # "astime": astime,
            "asstatus": asstatus,
            "alesson_id": alesson_id,
            "asuser_id": asuser_id
        })


class TeacherAttendanceGetView(GenericAPIView):
    """
    教师考勤管理  按学号查询
    """

    def get(self, request, teacher_id):
        """
        根据路由中班级id获取相关学生考勤

        路由: GET attendance/tea_attendance/(?P<teacher_id>\d+)/
        """
        try:
            tea_attendance = teacher_attendance_table.objects.filter(atuser_id=teacher_id)
        except:
            return Response({"error": "查询失败"})

        # 序列化
        tea_attendance_serializer = TeacherAttendanceSerializer(tea_attendance, many=True)
        tea_attendance_dict = tea_attendance_serializer.data

        return Response(tea_attendance_dict)

    # def patch(self, request, teacher_id):
    #     """局部修改"""
    #     try:
    #         tea_attendance = teacher_attendance_table.objects.get(atuser_id=teacher_id)
    #     except:
    #         return Response({"error": "查询错误"})
    #
    #     # 接收
    #     tea_attendance_dict = request.data
    #
    #     # print(stu_attendance)
    #
    #     # 验证
    #     tea_attendance_serilizer = TeacherAttendanceSerializer(tea_attendance, data=tea_attendance_dict, partial=True)
    #     if not tea_attendance_serilizer.is_valid():
    #         return Response(tea_attendance_serilizer.errors)
    #
    #     # 保存  update
    #     tea_attendance = tea_attendance_serilizer.save()
    #
    #     # 响应
    #     tea_attendance_serilizer = TeacherAttendanceSerializer(tea_attendance)
    #     tea_attendance_dict = tea_attendance_serilizer.data
    #     return Response(tea_attendance_dict, status=201)

    def delete(self, request, teacher_id):
        """删除"""
        try:
            tea_attendance = teacher_attendance_table.objects.get(atuser_id=teacher_id)
        except:
            return Response({"error": "查询错误"})

        # 删除
        tea_attendance.delete()

        # 响应
        return Response(status=204)


class TeacherAttendancePostView(GenericAPIView):
    """
    创建教师考勤信息
    路由: POST attendance/tea_attendance/
    """

    def post(self, request):
        """创建考勤信息"""
        # 获取请求参数
        tea_attendance = request.data

        # atid = tea_attendance.getlist("atid")[0]
        # attime = tea_attendance.getlist("attime")[0]
        atstatus = tea_attendance.getlist("atstatus")[0]
        alesson_id = tea_attendance.getlist("alesson_id")[0]
        # atuser_id = tea_attendance.getlist("atuser_id")[0]

        # 获取该课老师id
        lesson_info = lesson_table.objects.filter(lid=alesson_id)
        lesson_serilizer = LessonSerializer(lesson_info, many=True)
        lesson_list = lesson_serilizer.data
        atuser_id = lesson_list[0]["lteacher"]

        # 将获取的数据上在数据库创建
        teacher_attendance_table.objects.create(
            # atid=atid,
            atstatus=atstatus,
            alesson_id=alesson_id,
            atuser_id=atuser_id
        )

        return Response({
            # "atid": atid,
            "atstatus": atstatus,
            "alesson_id": alesson_id,
            "atuser_id": atuser_id
        })
