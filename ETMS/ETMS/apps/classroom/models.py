from django.db import models


class classroom_table(models.Model):
    """实验室表"""

    SIZE_CHOICES = (  # 实验室大小
        (0, '小'),
        (1, '中'),
        (2, '大'),
        (3, '超大'),
    )

    crid = models.IntegerField(primary_key=True, verbose_name="实验室号")
    crname = models.CharField(max_length=20, verbose_name="实验室名")
    crsize = models.SmallIntegerField(choices=SIZE_CHOICES, default=0, verbose_name='实验室规格')
    crdevice = models.IntegerField(default=0, verbose_name="设备个数")

    class Meta:
        db_table = "t_classroom"
        verbose_name = "实验室"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.crname
