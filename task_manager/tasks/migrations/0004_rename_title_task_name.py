# Generated by Django 5.2 on 2025-04-19 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='name',
        ),
    ]
