# Generated by Django 2.0.4 on 2018-06-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180621_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='status',
        ),
    ]
