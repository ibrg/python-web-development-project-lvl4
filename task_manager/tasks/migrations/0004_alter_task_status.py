# Generated by Django 4.1.7 on 2023-03-25 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        ('tasks', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='statuses.status'),
        ),
    ]