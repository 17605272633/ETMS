from django.db import models
from django.utils import timezone
from classes.models import class_table

from users.models import teacher_table


class lesson_table(models.Model):
    """课程表"""
    lid = models.IntegerField(primary_key=True, verbose_name="课程号")
    lname = models.CharField(max_length=20, verbose_name="课程名")
    ltime = models.IntegerField(verbose_name="课程时间(周)")
    lclass = models.ForeignKey(class_table, on_delete=models.CASCADE, verbose_name="班级课程")
    lstart = models.DateTimeField(default=timezone.now, verbose_name="课程开始时间")
    lend = models.DateTimeField(default=timezone.now, verbose_name="课程结束时间")
    lteacher = models.ForeignKey(teacher_table, on_delete=models.CASCADE, verbose_name="课程老师")

    class Meta:
        db_table = "t_lesson"
        verbose_name = "课程表"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.lname
