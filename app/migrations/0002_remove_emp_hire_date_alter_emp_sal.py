# Generated by Django 4.2.7 on 2023-12-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='hire_date',
        ),
        migrations.AlterField(
            model_name='emp',
            name='sal',
            field=models.BigIntegerField(),
        ),
    ]
