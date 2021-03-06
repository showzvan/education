# Generated by Django 2.1.5 on 2019-01-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorCates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catename', models.CharField(max_length=255, verbose_name='专业分类名')),
                ('pid', models.IntegerField(verbose_name='父分类')),
                ('is_status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '专业分类',
                'verbose_name_plural': '专业分类',
                'db_table': 'zhouju_major_cates',
            },
        ),
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_desciption', models.CharField(max_length=255, null=True, verbose_name='专业简述')),
                ('level', models.IntegerField(default=0, verbose_name='层次')),
                ('major_name', models.CharField(max_length=255, verbose_name='专业名称')),
                ('is_recommend', models.IntegerField(default=1, verbose_name='是否推荐')),
                ('times', models.FloatField(verbose_name='学制')),
                ('count', models.BigIntegerField(verbose_name='报读人数')),
                ('is_fast', models.BooleanField(default=False, verbose_name='是否录取快')),
                ('is_special', models.BooleanField(default=False, verbose_name='是否特色专业')),
                ('detail', models.TextField(verbose_name='专业介绍')),
                ('is_status', models.BooleanField(default=True, verbose_name='状态')),
                ('major_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='major.MajorCates', verbose_name='所属分类')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.Schools', verbose_name='所属院校')),
            ],
            options={
                'verbose_name': '专业信息',
                'verbose_name_plural': '专业信息',
                'db_table': 'zhouju_majors',
            },
        ),
    ]
