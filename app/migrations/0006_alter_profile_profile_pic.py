# Generated by Django 4.0.5 on 2022-06-08 21:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_post_image_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png', max_length=255),
        ),
    ]
