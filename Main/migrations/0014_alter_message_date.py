# Generated by Django 3.2.3 on 2021-06-18 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 6, 18, 9, 15, 43, 865886)),
        ),
    ]
