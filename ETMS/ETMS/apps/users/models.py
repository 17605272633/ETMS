from django.db import models


# Create your models here.
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
