from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models import student_attendance_table, teacher_attendance_table
from attendance.serializers import StudentAttendanceSerializer, TeacherAttendanceSerializer
from lesson.models import lesson_table
from lesson.serializers import LessonSerializer
from users.models import teacher_table, student_table
from users.serializers import TeacherSerializer, StudentSerializer


class AttendanceGetView(GenericAPIView):
    """
    学生考勤管理  按学号查询
    """

    def post(self, request):
        """
        根据路由中班级id获取相关学生考勤

        路由: POST attendance/user_attendance/

        请求: user_id = ?   usrkind = ?

        """
        # 获取请求参数
        attendance = request.data

        userkind = attendance.getlist("userkind")[0]
        user_id = attendance.getlist("user_id")[0]

        # 教师
        if userkind == "1":

            try:
                user_attendance = teacher_attendance_table.objects.filter(atuser_id=user_id)
            except:
                return Response({"error": "查询失败"})

            # 序列化
            tea_attendance_serializer = TeacherAttendanceSerializer(user_attendance, many=True)
            tea_attendance_dict = tea_attendance_serializer.data

            attendance_list = []

            for dict1 in tea_attendance_dict:
                id = dict1["id"]
                time = dict1["attime"]
                status = dict1["atstatus"]
                lesson_id = dict1["alesson"]
                user_id = dict1["atuser"]

                if status == 1:
                    status = "全勤"
                elif status == 2:
                    status = "迟到"
                elif status == 3:
                    status = "早退"
                elif status == 4:
                    status = "缺勤"
                elif status == 5:
                    status = "请假"

                # 获取老师姓名
                teacher = teacher_table.objects.filter(tid=user_id)
                teacher_data = TeacherSerializer(teacher, many=True)
                teacher_name = teacher_data.data[0]["tname"]

                # 获取课程名
                lesson = lesson_table.objects.filter(lid=lesson_id)
                lesson_data = LessonSerializer(lesson, many=True)
                lesson_name = lesson_data.data[0]["lname"]

                data = {
                    "id": id,
                    "name": teacher_name,
                    "time": time,
                    "lesson_name": lesson_name,
                    "status": status,
                }

                attendance_list.append(data)

            return Response(attendance_list)

        # 学生
        if userkind == "2":
            try:
                user_attendance = student_attendance_table.objects.filter(asuser_id=user_id)
            except:
                return Response({"error": "查询失败"})

            # 序列化
            stu_attendance_serializer = StudentAttendanceSerializer(user_attendance, many=True)
            stu_attendance_dict = stu_attendance_serializer.data

            attendance_list = []

            for dict1 in stu_attendance_dict:
                id = dict1["id"]
                time = dict1["astime"]
                status = dict1["asstatus"]
                lesson_id = dict1["alesson"]
                user_id = dict1["asuser"]

                if status == 1:
                    status = "全勤"
                elif status == 2:
                    status = "迟到"
                elif status == 3:
                    status = "早退"
                elif status == 4:
                    status = "缺勤"
                elif status == 5:
                    status = "请假"

                # 获取学生姓名
                student = student_table.objects.filter(sid=user_id)
                student_data = StudentSerializer(student, many=True)
                student_name = student_data.data[0]["sname"]

                # 获取课程名
                lesson = lesson_table.objects.filter(lid=lesson_id)
                lesson_data = LessonSerializer(lesson, many=True)
                lesson_name = lesson_data.data[0]["lname"]

                data = {
                    "id": id,
                    "name": student_name,
                    "time": time,
                    "lesson_name": lesson_name,
                    "status": status,
                }

                attendance_list.append(data)

            return Response(attendance_list)

    # def delete(self, request, student_id):
    #     """删除"""
    #     try:
    #         stu_attendance = student_attendance_table.objects.get(asuser_id=student_id)
    #     except:
    #         return Response({"error": "查询错误"})
    #
    #     # 删除
    #     stu_attendance.delete()
    #
    #     # 响应
    #     return Response(status=204)


class AttendanceUploadView(APIView):
    """
    局部更新考勤信息
    路由: POST attendance/up_attendance/
    """

    def post(self, request):
        # 获取请求参数
        attendance = request.data

        id = attendance.getlist("id")[0]
        userkind = attendance.getlist("userkind")[0]
        status = attendance.getlist("status")[0]

        # 教师
        if userkind == "1":

            try:
                tea_attendance = teacher_attendance_table.objects.get(id=id)
            except:
                return Response({"error": "查询错误"})

            tea_attendance.atstatus = status
            print(status)
            tea_attendance.save()

            return Response({"message": "ok"}, status=201)

        # 学生
        if userkind == "2":

            try:
                stu_attendance = student_attendance_table.objects.get(id=id)
            except:
                return Response({"error": "查询错误"})

            stu_attendance.asstatus = status
            stu_attendance.save()

            return Response({"message": "ok"}, status=201)


class AttendanceCreateView(APIView):
    """
    创建考勤信息
    路由: POST attendance/attendance/
    """

    def post(self, request):
        """创建考勤信息"""
        # 获取请求参数
        attendance = request.data

        userkind = attendance.getlist("userkind")[0]

        # 教师
        if userkind == "1":
            tea_lesson_id = attendance.getlist("lesson_id")[0]
            tea_user_id = attendance.getlist("user_id")[0]

            # 将获取的数据上在数据库创建
            teacher_attendance_table.objects.create(
                atstatus=1,
                alesson_id=tea_lesson_id,
                atuser_id=tea_user_id
            )

            return Response({
                "message": "ok"
            })

        # 学生
        if userkind == "2":
            stu_lesson_id = attendance.getlist("lesson_id")[0]
            stu_user_id = attendance.getlist("user_id")[0]

            # 将获取的数据上在数据库创建
            student_attendance_table.objects.create(

                asstatus=1,
                alesson_id=stu_lesson_id,
                asuser_id=stu_user_id
            )

            return Response({
                "message": "ok"
            })


class TeacherAttendanceGetView(GenericAPIView):
    """
    教师考勤管理  按工号查询
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

#
# class TeacherAttendancePostView(GenericAPIView):
#     """
#     创建教师考勤信息
#     路由: POST attendance/tea_attendance/
#     """
#
#     def post(self, request):
#         """创建考勤信息"""
#         # 获取请求参数
#         tea_attendance = request.data
#
#         # atid = tea_attendance.getlist("atid")[0]
#         # attime = tea_attendance.getlist("attime")[0]
#         atstatus = tea_attendance.getlist("atstatus")[0]
#         alesson_id = tea_attendance.getlist("alesson_id")[0]
#         # atuser_id = tea_attendance.getlist("atuser_id")[0]
#
#         # 获取该课老师id
#         lesson_info = lesson_table.objects.filter(lid=alesson_id)
#         lesson_serilizer = LessonSerializer(lesson_info, many=True)
#         lesson_list = lesson_serilizer.data
#         atuser_id = lesson_list[0]["lteacher"]
#
#         # 将获取的数据上在数据库创建
#         teacher_attendance_table.objects.create(
#             # atid=atid,
#             atstatus=atstatus,
#             alesson_id=alesson_id,
#             atuser_id=atuser_id
#         )
#
#         return Response({
#             # "atid": atid,
#             "atstatus": atstatus,
#             "alesson_id": alesson_id,
#             "atuser_id": atuser_id
#         })
