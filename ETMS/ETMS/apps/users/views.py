from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import super_table, teacher_table, student_table
from users.serializers import SuperSerializer, TeacherSerializer, StudentSerializer


class UserManagementView(APIView):
    """用户管理"""

    def get(self, request):
        """返回"""
        # 去 session 中取指定的值
        user_id = request.session.get("user_id", None)
        is_admin = request.session.get("is_admin", False)

        # 如果用户id存在，并且是管理员，那么直接跳转管理后台主页
        if user_id and is_admin:
            return render(request, "html/super_index.html")

        return render(request, "html/admin_login.html")

    def post(self, request):
        # 获取请求参数
        user_info = request.data

        username = user_info.getlist("username")[0]
        password = user_info.getlist("password")[0]
        userkind = user_info.getlist("userkind")[0]

        # 判断是否存在

        if userkind == "3":
            # 超级管理员

            try:
                user = super_table.objects.filter(username=username)
            except:
                return Response({"error": "登陆错误"})

            user_serializer = SuperSerializer(user, many=True)

            # 获取序列化后的用户密码
            user_data = user_serializer.data

            # 从数据中获取数据
            user_info = user_data[0]
            user_password = user_info["password"]

            if password != user_password:
                return Response({"error": "登陆错误"})

            else:
                request.session['user_id'] = user_info["username"]
                request.session['is_admin'] = True

                return render(request, "html/super_index.html")

        if userkind == "1":
            # 教师

            try:
                user = teacher_table.objects.filter(tid=username)
            except:
                return Response({"error": "登陆错误"})

            if not user:
                return Response({"error": "登陆错误"})

            if password != username:
                return Response({"error": "登陆错误"})

            else:
                user_serializer = TeacherSerializer(user, many=True)

                # 获取序列化后的数据
                user_data = user_serializer.data

                # 获取具体数据
                user_info = user_data[0]

                request.session['user_id'] = user_info["tid"]
                request.session['is_admin'] = False

                return render(request, "html/teacher_index.html")

        if userkind == "2":
            # 学生

            try:
                user = student_table.objects.filter(sid=username)
            except:
                return Response({"error": "登陆错误"})

            if not user:
                return Response({"error": "登陆错误"})

            if password != username:
                return Response({"error": "登陆错误"})

            else:
                user_serializer = StudentSerializer(user, many=True)

                # 获取序列化后的数据
                user_data = user_serializer.data

                # 获取具体数据
                user_info = user_data[0]

                request.session['user_id'] = user_info["sid"]
                request.session['is_admin'] = False

                return render(request, "html/student_index.html")


class SupermanagementView(APIView):
    """超级管理员用户管理"""

    def get(self, request, userkind):
        """查询所有"""

        # 获取查询用户种类
        # 教师
        if userkind == "1":
            try:
                user = teacher_table.objects.all()
            except:
                return Response({"error": "查询失败"})

            # 序列化
            user_serializer = TeacherSerializer(user, many=True)
            classroom_dict = user_serializer.data

            # 返回
            return Response(classroom_dict)

        # 学生
        elif userkind == "2":
            try:
                user = student_table.objects.all()
            except:
                return Response({"error": "查询失败"})

            # 序列化
            user_serializer = StudentSerializer(user, many=True)
            user_dict = user_serializer.data

            # 返回
            return Response(user_dict)

    def post(self, request):
        """创建"""
        # 获取请求参数
        user_info = request.data

        # 获取创建的用户种类
        userkind = user_info.getlist("userkind")[0]

        # 教师
        if userkind == "1":

            # 获取其余信息
            tid = user_info.getlist("tid")[0]
            tname = user_info.getlist("tname")[0]

            # 将获取的数据上在数据库创建
            teacher_table.objects.create(
                tid=tid,
                tname=tname,
            )

            return Response({
                "tid": tid,
                "tname": tname,
            })

        elif userkind == "2":

            # 获取其余信息
            sid = user_info.getlist("sid")[0]
            sname = user_info.getlist("sname")[0]
            sclass_id = user_info.getlist("sclass_id")[0]

            # 将获取的数据上在数据库创建
            teacher_table.objects.create(
                sid=sid,
                sname=sname,
                sclass_id=sclass_id,
            )

            return Response({
                "sid": sid,
                "sname": sname,
                "sclass_id": sclass_id,
            })

    def put(self, request, userkind, id):
        """修改"""

        # 教师
        if userkind == "1":

            try:
                user = teacher_table.objects.get(tid=id)
            except:
                return Response({"error": "查询错误"})

            # 接收
            user_dict = request.data

            # 验证
            user_serilizer = TeacherSerializer(user, data=user_dict)

            if not user_serilizer.is_valid():
                return Response(user_serilizer.errors)

            # 保存  update
            user = user_serilizer.save()

            # 响应
            user_serilizer = TeacherSerializer(user)
            user_dict = user_serilizer.data
            return Response(user_dict, status=201)

        # 学生
        if userkind == "2":

            try:
                user = student_table.objects.get(sid=id)
            except:
                return Response({"error": "查询错误"})

            # 接收
            user_dict = request.data

            # 验证
            user_serilizer = StudentSerializer(user, data=user_dict)

            if not user_serilizer.is_valid():
                return Response(user_serilizer.errors)

            # 保存  update
            user = user_serilizer.save()

            # 响应
            user_serilizer = StudentSerializer(user)
            user_dict = user_serilizer.data
            return Response(user_dict, status=201)

    def patch(self, request, userkind, id):
        """局部更新"""

        # 教师
        if userkind == "1":

            try:
                user = teacher_table.objects.get(tid=id)
            except:
                return Response({"error": "查询错误"})

            # 接收
            user_dict = request.data

            # 验证
            user_serilizer = TeacherSerializer(user, data=user_dict, partial=True)

            if not user_serilizer.is_valid():
                return Response(user_serilizer.errors)

            # 保存  update
            user = user_serilizer.save()

            # 响应
            user_serilizer = TeacherSerializer(user)
            user_dict = user_serilizer.data
            return Response(user_dict, status=201)

        # 学生
        if userkind == "2":

            try:
                user = student_table.objects.get(sid=id)
            except:
                return Response({"error": "查询错误"})

            # 接收
            user_dict = request.data

            # 验证
            user_serilizer = StudentSerializer(user, data=user_dict, partial=True)

            if not user_serilizer.is_valid():
                return Response(user_serilizer.errors)

            # 保存  update
            user = user_serilizer.save()

            # 响应
            user_serilizer = StudentSerializer(user)
            user_dict = user_serilizer.data
            return Response(user_dict, status=201)

    def delete(self, request, userkind, id):
        """删除"""

        if userkind == "1":
            try:
                user = teacher_table.objects.get(tid=id)
            except:
                return Response({"error": "查询错误"})

            # 删除
            user.delete()

            # 响应
            return Response(status=204)

        if userkind == "2":
            try:
                user = student_table.objects.get(sid=id)
            except:
                return Response({"error": "查询错误"})

            # 删除
            user.delete()

            # 响应
            return Response(status=204)


class UserLogOutView(APIView):
    """用户管理退出"""

    def get(self, request):
        request.session.pop('user_id', None)
        request.session.pop('is_admin', None)

        # 返回结果
        return HttpResponseRedirect("http://www.etms.mp:8000/user/user/")


class StudentView(APIView):
    """
    学生视图
    """

    def post(self, request):
        """
        创建学生信息
        路由: POST /user/student/
        """

        student_info = request.data

        user_id = student_info.getlist("user_id")[0]
        user_name = student_info.getlist("user_name")[0]
        class_id = student_info.getlist("class_id")[0]

        student_table.objects.create(
            sid=user_id,
            sname=user_name,
            sclass_id=class_id
        )

        return Response({"message": "ok"})

    def delete(self, request):
        """删除学生信息路由: DELETE /user/student/"""
        student_info = request.data

        user_id = student_info.getlist("user_id")[0]

        try:
            user = student_table.objects.get(sid=user_id)
        except:
            return Response({"error": "查询错误"})

        # 删除
        user.delete()

        # 响应
        return Response(status=204)


class StudentFindView(APIView):
    """学生信息查询"""

    def post(self, request):
        classes_info = request.data

        classes_id = classes_info.getlist("classes_id")[0]

        print(classes_id)

        user = student_table.objects.filter(sclass_id=classes_id)
        print(user)

        user_serializer = StudentSerializer(user, many=True)

        # 获取序列化后的用户密码
        user_data = user_serializer.data

        return Response(user_data)


class TeacherView(APIView):
    """
    教师视图
    """

    def get(self, request):
        teacher = teacher_table.objects.filter()
        teacher_info = TeacherSerializer(teacher, many=True)

        return Response(teacher_info.data)

    def post(self, request):
        """
        创建教师信息
        路由: POST /user/teacher/
        """

        student_info = request.data

        user_id = student_info.getlist("user_id")[0]
        user_name = student_info.getlist("user_name")[0]

        teacher_table.objects.create(
            tid=user_id,
            tname=user_name,

        )

        return Response({"message": "ok"})

    def delete(self, request):
        """
        删除学生信息
        路由: DELETE /user/teacher/
        """
        teacher_info = request.data

        user_id = teacher_info.getlist("user_id")[0]

        try:
            user = teacher_table.objects.get(tid=user_id)
        except:
            return Response({"error": "查询错误"})

        # 删除
        user.delete()

        # 响应
        return Response(status=204)
