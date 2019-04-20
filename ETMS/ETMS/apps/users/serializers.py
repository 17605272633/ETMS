from rest_framework import serializers

from users.models import student_table


class StudentSerializer(serializers.ModelSerializer):
    """班级表序列化器"""

    # sid = serializers.IntegerField(label='班id', read_only=True)
    # sname = serializers.CharField(label='班名', max_length=20)
    # sclass = serializers.PrimaryKeyRelatedField(label='所属专业', queryset=profession_table.objects.all())

    class Meta:
        model = student_table
        fields = '__all__'
