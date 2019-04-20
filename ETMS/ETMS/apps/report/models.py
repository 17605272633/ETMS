from django.db import models
from django.utils import timezone

from classes.models import class_table
from users.models import student_table


class report_table(models.Model):
    """实验报告表"""
    # rid = models.IntegerField(primary_key=True, verbose_name="报告id")
    rname = models.CharField(max_length=20, verbose_name="报告名")
    rtime = models.DateTimeField(auto_now_add=True, verbose_name="实验报告提交时间")
    rfiles = models.CharField(max_length=200, verbose_name="上传地址")
    rstudent = models.ForeignKey(student_table, on_delete=models.CASCADE, verbose_name="学生")
    rclass = models.ForeignKey(class_table, on_delete=models.CASCADE, verbose_name="班级")

    class Meta:
        db_table = "t_report"  # 指定系别数据库名
        verbose_name = "实验报告"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.rname
