from rest_framework import serializers
from classes.models import class_table
from lesson.models import lesson_table
from users.models import teacher_table


class LessonSerializer(serializers.ModelSerializer):
    """专业表序列化器"""

    # lid = serializers.IntegerField(label='课程id',read_only=True)
    # lname = serializers.CharField(label='课程名', max_length=20)
    # ltime = serializers.IntegerField(verbose_name="课程时间(周)")
    # lclass = serializers.PrimaryKeyRelatedField(label='所属班级', queryset=class_table.objects.all())
    # lstart = serializers.DateTimeField(label='开始时间')
    # lend = serializers.DateTimeField(label="结束时间")
    # lteacher = serializers.PrimaryKeyRelatedField(label='代课老师', queryset=teacher_table.objects.all())

    class Meta:
        model = lesson_table
        fields = '__all__'





