# Generated by Django 3.0 on 2021-02-17 21:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screenshot',
            old_name='color',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='name',
        ),
        migrations.RemoveField(
            model_name='screenshot',
            name='ripe',
        ),
        migrations.AddField(
            model_name='screenshot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screenshot',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='imagefile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
