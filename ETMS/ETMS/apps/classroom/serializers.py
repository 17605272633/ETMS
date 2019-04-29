from rest_framework import serializers

from classroom.models import classroom_table


class ClassRoomSerializer(serializers.ModelSerializer):
    """实验室表序列化器"""

    # crid = serializers.IntegerField(primary_key=True, label="实验室号")
    # crname = serializers.CharField(max_length=20, label="实验室名")
    # crsize = serializers.IntegerField(choices=SIZE_CHOICES, default=0, label='实验室规格')
    # crdevice = serializers.IntegerField(default=0, label="设备个数")

    class Meta:
        model = classroom_table
        fields = '__all__'
