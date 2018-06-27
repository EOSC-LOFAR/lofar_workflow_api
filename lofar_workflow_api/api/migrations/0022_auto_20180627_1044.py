# Generated by Django 2.0.4 on 2018-06-27 08:44

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20180626_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='observation',
            field=models.CharField(default='someobs', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='config',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='pipeline',
            field=models.CharField(max_length=100),
        ),
    ]
