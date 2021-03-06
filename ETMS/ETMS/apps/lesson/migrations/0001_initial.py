# Generated by Django 2.1.7 on 2019-05-09 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lesson_table',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False, verbose_name='课程号')),
                ('lname', models.CharField(max_length=20, verbose_name='课程名')),
                ('ltime', models.IntegerField(verbose_name='课时')),
                ('lstart', models.DateTimeField(default=django.utils.timezone.now, verbose_name='课程开始日期')),
                ('lclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class_table', verbose_name='班级课程')),
                ('lclassroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom_table', verbose_name='课程实验室')),
            ],
            options={
                'verbose_name': '课程表',
                'db_table': 't_lesson',
            },
        ),
    ]
