from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    """系表序列化器"""

    # did = serializers.IntegerField(label='系id', read_only=True)
    # dname = serializers.CharField(label='系名', max_length=20)

    class Meta:
        model = department_table
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    """专业表序列化器"""

    # pid = serializers.IntegerField(label='专业id', read_only=True)
    # pname = serializers.CharField(label='专业名', max_length=20)
    # pdepart = serializers.PrimaryKeyRelatedField(label='所属系', queryset=department_table.objects.all())

    class Meta:
        model = profession_table
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    """班级表序列化器"""

    # cid = serializers.IntegerField(label='班id', read_only=True)
    # cname = serializers.CharField(label='班名', max_length=20)
    # cprofession = serializers.PrimaryKeyRelatedField(label='所属专业', queryset=profession_table.objects.all())

    class Meta:
        model = class_table
        fields = '__all__'


class ClassShowSerializer(serializers.Serializer):
    pid = serializers.IntegerField(label='专业id', read_only=True)
    pname = serializers.CharField(label='专业名', max_length=20)
    pclass = ClassSerializer(many=True)

    """
    [
        {
            "pid": 80901,
            "pname":"计算机科学与技术",
            "pclass":[
                        {
                            "cid":1530501,
                            "cname":"2015计算机科学与技术一班",
                            "ccount": 30
                        },
                        ......                                   
                    ]
        },
        ......         
    ]
    """




