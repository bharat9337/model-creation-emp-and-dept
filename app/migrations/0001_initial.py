# Generated by Django 4.2.7 on 2023-12-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('dept_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('d_loc', models.CharField(max_length=100)),
                ('hod', models.CharField(max_length=100)),
                ('dno', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('sal', models.BigIntegerField(max_length=100)),
                ('empno', models.BigIntegerField()),
                ('mgr', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
