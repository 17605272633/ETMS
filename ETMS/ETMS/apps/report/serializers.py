from rest_framework import serializers

from report.models import report_table


class ReportSerializer(serializers.ModelSerializer):
    """实验报告序列化器"""

    # 定义属性
    # rid = serializers.IntegerField(label="报告id",read_only=True)
    # rname = serializers.CharField(label="报告名")
    # rtime = serializers.DateTimeField(label="实验报告提交时间")
    # rfiles = serializers.CharField(label="上传地址")
    # lteacher = serializers.PrimaryKeyRelatedField(label='代课老师', queryset=teacher_table.objects.all())

    class Meta:
        model = report_table
        fields = '__all__'


class ReportResponseSerializer(serializers.ModelSerializer):
    """报告视图返回数据序列化器"""
    student_name = serializers.CharField(label='学生名', max_length=20)
    student_id = serializers.IntegerField(label='学号', read_only=True)
    report_name = serializers.CharField(label='报告名', max_length=200)
    upload_time = serializers.DateTimeField(label="上传时间")
    download_url = serializers.CharField(label='下载地址', max_length=200)