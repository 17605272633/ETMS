# Generated by Django 2.1.7 on 2019-05-18 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0002_lesson_table_lteacher'),
        ('users', '0002_super_table'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='report_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=20, verbose_name='报告名')),
                ('rtime', models.DateTimeField(auto_now_add=True, verbose_name='实验报告提交时间')),
                ('rfiles', models.CharField(max_length=200, verbose_name='上传地址')),
                ('rclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_table', verbose_name='班级')),
                ('rlesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson_table', verbose_name='课程')),
                ('rstudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student_table', verbose_name='学生')),
            ],
            options={
                'db_table': 't_report',
                'verbose_name': '实验报告',
            },
        ),
    ]
