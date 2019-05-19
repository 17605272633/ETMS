from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response

from ETMS import settings
from ETMS.utils.report_storage import storage
from report.models import report_table
from report.serializers import ReportSerializer
from users.models import student_table
from users.serializers import StudentSerializer


class ReportShowView(GenericAPIView, ListModelMixin):
    """
    获取实验报告数据视图
    路由：POST  /report/report/

    参数: class_id	int	是	类别id（班级id）

    返回json: [
              {
                "id": 3,
                "rname": "3333333333333333333",
                "rtime": "2019-04-11T21:56:27+08:00",
                "rfiles": "333333333",
                "rstudent": 201530050205,
                "rlesson": 000000,
                "rclass": 000000,
              },
              {
              }.
              ...
            ]

    """

    def post(self, request):
        # 获取请求参数
        querydict = request.data

        # 获取报告名,所属学生,所在班级
        lesson_id = querydict.getlist("lesson_id")[0]

        select_profession = report_table.objects.filter(rlesson_id=lesson_id)
        serializer = ReportSerializer(select_profession, many=True)

        report_data = serializer.data

        # 准备一个空列表装数据
        report_list = []

        for dict1 in report_data:
            # 获取报告名
            report_name = dict1["rname"]
            # 获取报告上传时间
            upload_time = dict1["rtime"]
            # 获取报告链接
            download_url = dict1["rfiles"]
            # 获取学生学号
            student_id = dict1["rstudent"]

            # 获取学生姓名
            student = student_table.objects.filter(sid=student_id)
            student_data = StudentSerializer(student, many=True)

            student_name = student_data.data[0]["sname"]

            data = {
                "student_name": student_name,
                "student_id": student_id,
                "report_name": report_name,
                "upload_time": upload_time,
                "download_url": download_url
            }

            report_list.append(data)

        return Response(report_list)


class ReportAddView(GenericAPIView, CreateModelMixin):
    """
    实验报告添加视图
    路由：POST /report/reportadd/

    请求参数: {
            rname
            rfiles
            rclass_id
            rstudent_id
            }

    """
    serializer_class = ReportSerializer

    def post(self, request, *args, **kwargs):
        # 获取请求参数
        querydict = request.data

        # 获取报告名,所属学生,所在班级
        rname = querydict.getlist("rname")[0]
        rclass = querydict.getlist("rclass")[0]
        rstudent = querydict.getlist("rstudent")[0]
        rlesson = querydict.getlist("rlesson")[0]

        # 获取到上传的文件
        rfile_obj = request.FILES.get("rfiles")

        f1 = open(rfile_obj.name, "wb")

        for i in rfile_obj.chunks():
            f1.write(i)

        f1.close()

        file_object = open(rfile_obj.name, 'rb')
        file_context = file_object.read()  # file_context是一个string，读取完后，就失去了对test.txt的文件引用
        #  file_context = open(file).read().splitlines()
        # file_context是一个list，每行文本内容是list中的一个元素

        # 再将文件上传到七牛云并获取路径
        report_files_url = storage(file_context)

        file_object.close()

        encodeurl = (settings.QINIU_DOMIN_PREFIX + report_files_url).encode()

        # 将获取的数据上在数据库创建
        report_table.objects.create(
            rname=rname,
            rfiles=settings.QINIU_DOMIN_PREFIX + report_files_url + "?attname=",
            rstudent_id=rstudent,
            rlesson_id=rlesson,
            rclass_id=rclass,
        )

        return Response({
            "message": "ok"
        })
