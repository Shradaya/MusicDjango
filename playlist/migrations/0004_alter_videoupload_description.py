# Generated by Django 3.2.3 on 2021-05-26 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_videoupload_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoupload',
            name='Description',
            field=models.TextField(max_length=750),
        ),
    ]