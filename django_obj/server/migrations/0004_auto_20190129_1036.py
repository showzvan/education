# Generated by Django 2.1.5 on 2019-01-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20190129_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aquestions',
            name='leval',
            field=models.CharField(choices=[('gqz', '高起专'), ('gqb', '高起本'), ('zsb', '专升本')], default='gqb', max_length=3, verbose_name='所属层次'),
        ),
    ]
