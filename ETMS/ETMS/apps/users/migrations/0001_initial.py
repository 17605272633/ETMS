# Generated by Django 2.1.7 on 2019-04-09 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_table',
            fields=[
                ('sid', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='学号')),
                ('sname', models.CharField(max_length=20, verbose_name='学生名')),
                ('lesson', models.ManyToManyField(to='lesson.lesson_table')),
                ('sclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_table', verbose_name='所在班级')),
            ],
            options={
                'verbose_name': '学生表',
                'db_table': 't_student',
            },
        ),
        migrations.CreateModel(
            name='teacher_table',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False, verbose_name='教师工号')),
                ('tname', models.CharField(max_length=20, verbose_name='教师名')),
            ],
            options={
                'verbose_name': '教师表',
                'db_table': 't_teacher',
            },
        ),
    ]
