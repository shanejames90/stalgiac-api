# Generated by Django 3.0 on 2021-02-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210223_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='sspic',
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='imagefile',
            field=models.ImageField(blank=True, null=True, upload_to='screenshots/'),
        ),
    ]
