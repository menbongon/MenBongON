# Generated by Django 2.2.5 on 2019-09-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='realname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
