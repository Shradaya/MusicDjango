# Generated by Django 3.2.3 on 2021-05-27 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 5, 27, 9, 20, 19, 332714)),
        ),
    ]
