# Generated by Django 2.1.7 on 2019-05-09 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_attendance_table',
            name='atuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher_table', verbose_name='教师'),
        ),
        migrations.AddField(
            model_name='student_attendance_table',
            name='asuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student_table', verbose_name='学生'),
        ),
    ]