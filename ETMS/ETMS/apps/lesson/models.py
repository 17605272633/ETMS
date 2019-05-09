from django.db import models
from django.utils import timezone
from classes.models import class_table


class lesson_table(models.Model):
    """课程表"""
    # WEEKTIME_CHOICES = (
    #     (0, '未指定周课程'),
    #     (1, '星期一'),
    #     (2, '星期二'),
    #     (3, '星期三'),
    #     (4, '星期四'),
    #     (5, '星期五'),
    #     (6, '星期六'),
    #     (7, '星期天'),
    # )
    #
    # DAYTIME_CHOICES = (
    #     (0, '未指定时间'),
    #     (1, '上午一二节课'),
    #     (2, '上午三四节课'),
    #     (3, '下午五六节课'),
    #     (4, '下午七八节课'),
    #     (5, '晚上九十节课'),
    # )

    lid = models.IntegerField(primary_key=True, verbose_name="课程号")
    lname = models.CharField(max_length=20, verbose_name="课程名")
    ltime = models.IntegerField(verbose_name="课时")
    lstart = models.DateTimeField(default=timezone.now, verbose_name="课程开始日期")
    lclass = models.ForeignKey(class_table, on_delete=models.CASCADE, verbose_name="班级课程")
    lteacher = models.ForeignKey('users.teacher_table', on_delete=models.CASCADE, verbose_name="课程老师")
    lclassroom = models.ForeignKey('classroom.classroom_table', on_delete=models.CASCADE, verbose_name="课程实验室")

    class Meta:
        db_table = "t_lesson"
        verbose_name = "课程表"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.lname
