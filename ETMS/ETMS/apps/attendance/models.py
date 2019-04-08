from django.db import models
from users.models import student_table, teacher_table


class student_attendance_table(models.Model):
    """学生考勤表"""

    STATUS_CHOICES = (
        (1, "全勤"),
        (2, "迟到"),
        (3, "早退"),
        (4, "缺勤"),
        (5, "请假"),
    )

    asid = models.IntegerField(primary_key=True, verbose_name="考勤id")
    astime = models.DateTimeField(auto_now_add=True, verbose_name="日期")
    asuser = models.ForeignKey(student_table, on_delete=models.CASCADE, verbose_name="学生")
    asstatus = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name="考勤信息")

    class Meta:
        db_table = "t_s_attendance"
        verbose_name = "学生考勤"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.astime


class teacher_attendance_table(models.Model):
    """教师考勤表"""

    STATUS_CHOICES = (
        (1, "全勤"),
        (2, "迟到"),
        (3, "早退"),
        (4, "缺勤"),
        (5, "请假"),
    )

    atid = models.IntegerField(primary_key=True, verbose_name="考勤id")
    attime = models.DateTimeField(auto_now_add=True, verbose_name="日期")
    atuser = models.ForeignKey(teacher_table, on_delete=models.CASCADE, verbose_name="教师")
    atstatus = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name="考勤信息")

    class Meta:
        db_table = "t_t_attendance"
        verbose_name = "教师考勤"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.attime