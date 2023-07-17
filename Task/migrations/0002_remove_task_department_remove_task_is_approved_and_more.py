# Generated by Django 4.0.1 on 2022-01-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='department',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.IntegerField(null=True, verbose_name='Assigned_to'),
        ),
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.CharField(max_length=500, null=True, verbose_name='description'),
        ),
    ]
