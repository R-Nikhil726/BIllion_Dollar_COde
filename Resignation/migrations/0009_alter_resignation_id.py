# Generated by Django 4.0.1 on 2022-01-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resignation', '0008_auto_20220118_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resignation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
