from django.db import models

from classes.models import class_table
from lesson.models import lesson_table


class teacher_table(models.Model):
    """教师表"""
    tid = models.IntegerField(primary_key=True, verbose_name="教师工号")
    tname = models.CharField(max_length=20, verbose_name="教师名")

    class Meta:
        db_table = "t_teacher"
        verbose_name = "教师表"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.tname


class student_table(models.Model):
    """学生表"""
    sid = models.BigIntegerField(primary_key=True, verbose_name="学号")
    sname = models.CharField(max_length=20, verbose_name="学生名")
    sclass = models.ForeignKey(class_table, on_delete=models.CASCADE, verbose_name="所在班级")
    lesson = models.ManyToManyField(lesson_table)

    class Meta:
        db_table = "t_student"
        verbose_name = "学生表"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.sname


class super_table(models.Model):
    """超级管理员表"""

    username = models.CharField(max_length=20, verbose_name="账号名")
    password = models.CharField(max_length=20, verbose_name="密码")

    class Meta:
        db_table = "t_super"
        verbose_name = "超级管理员表"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.username

