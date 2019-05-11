from rest_framework import serializers

from attendance.models import student_attendance_table, teacher_attendance_table


class StudentAttendanceSerializer(serializers.ModelSerializer):
    """学生考勤表序列化器"""

    # asid = serializers.IntegerField(primary_key=True, label="考勤id")
    # alesson = serializers.ForeignKey(lesson_table, on_delete=models.CASCADE, label="课程")
    # astime = serializers.DateTimeField(auto_now_add=True, label="日期")
    # asuser = serializers.ForeignKey(student_table, on_delete=models.CASCADE, label="学生")
    # asstatus = serializers.SmallIntegerField(choices=STATUS_CHOICES, default=1, label="考勤信息")
    #
    class Meta:
        model = student_attendance_table
        fields = '__all__'


class TeacherAttendanceSerializer(serializers.ModelSerializer):
    """教师考勤表序列化器"""

    # atid = serializers.IntegerField(primary_key=True, label="考勤id")
    # alesson = serializers.ForeignKey(lesson_table, on_delete=models.CASCADE, label="课程")
    # attime = serializers.DateTimeField(auto_now_add=True, label="日期")
    # atuser = serializers.ForeignKey(student_table, on_delete=models.CASCADE, label="教师")
    # atstatus = serializers.SmallIntegerField(choices=STATUS_CHOICES, default=1, label="考勤信息")
    #
    class Meta:
        model = teacher_attendance_table
        fields = '__all__'
