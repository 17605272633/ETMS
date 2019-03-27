from django.db import models


class department_table(models.Model):
    """系表"""
    did = models.IntegerField(primary_key=True, verbose_name="系号")
    dname = models.CharField(max_length=20, verbose_name="系名")

    class Meta:
        db_table = "t_department"  # 指定系别数据库名
        verbose_name = "系"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.dname


class profession_table(models.Model):
    """专业表"""
    pid = models.IntegerField(primary_key=True, verbose_name="专业号")
    pname = models.CharField(max_length=20, verbose_name="专业名")
    pdepart = models.ForeignKey(department_table, on_delete=models.CASCADE, verbose_name="所在系")

    class Meta:
        db_table = "t_profession"
        verbose_name = "专业"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.pname


class class_table(models.Model):
    cid = models.IntegerField(primary_key=True, verbose_name="班号")
    cname = models.CharField(max_length=20, verbose_name="班名")
    cprofession = models.ForeignKey(profession_table, on_delete=models.CASCADE, verbose_name="所在专业")

    class Meta:
        db_table = "t_class"
        verbose_name = "班级"

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.cname

