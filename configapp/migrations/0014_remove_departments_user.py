# Generated by Django 5.2 on 2025-05-07 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0013_remove_teacher_departments_departments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='user',
        ),
    ]
