# Generated by Django 2.2.3 on 2019-08-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190807_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_post',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
