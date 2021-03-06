# Generated by Django 4.0.5 on 2022-06-08 20:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_likes_post_remove_likes_user_likes_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='default.png', max_length=255),
        ),
    ]
