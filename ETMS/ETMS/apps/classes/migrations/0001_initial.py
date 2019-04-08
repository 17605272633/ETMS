# Generated by Django 2.1.7 on 2019-03-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='class_table',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False, verbose_name='班号')),
                ('cname', models.CharField(max_length=20, verbose_name='班名')),
            ],
            options={
                'db_table': 't_class',
                'verbose_name': '班级',
            },
        ),
        migrations.CreateModel(
            name='department_table',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False, verbose_name='系号')),
                ('dname', models.CharField(max_length=20, verbose_name='系名')),
            ],
            options={
                'db_table': 't_department',
                'verbose_name': '系',
            },
        ),
        migrations.CreateModel(
            name='profession_table',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='专业号')),
                ('pname', models.CharField(max_length=20, verbose_name='专业名')),
                ('pdepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.department_table', verbose_name='所在系')),
            ],
            options={
                'db_table': 't_profession',
                'verbose_name': '专业',
            },
        ),
        migrations.AddField(
            model_name='class_table',
            name='cprofession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.profession_table', verbose_name='所在专业'),
        ),
    ]