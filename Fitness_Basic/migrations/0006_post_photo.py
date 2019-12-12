# Generated by Django 2.1.1 on 2018-09-13 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness_Basic', '0005_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
