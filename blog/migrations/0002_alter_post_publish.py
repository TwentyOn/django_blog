# Generated by Django 5.1.6 on 2025-03-02 16:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 2, 16, 35, 8, 293779, tzinfo=datetime.timezone.utc)),
        ),
    ]
