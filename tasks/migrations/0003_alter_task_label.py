# Generated by Django 5.2 on 2025-04-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, related_name='tasks_label', to='labels.label', verbose_name='Метки'),
        ),
    ]
