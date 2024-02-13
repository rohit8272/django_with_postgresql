# Generated by Django 4.2.10 on 2024-02-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=3)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_gender', models.CharField()),
                ('emp_designation', models.CharField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
