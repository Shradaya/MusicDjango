# Generated by Django 3.2.3 on 2021-05-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=140)),
                ('Thumbnail', models.ImageField(upload_to='videoes/Thumbnail')),
                ('Video', models.FileField(upload_to='videoes/')),
            ],
        ),
    ]
