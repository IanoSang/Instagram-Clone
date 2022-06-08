# Generated by Django 4.0.5 on 2022-06-07 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_count', to='app.post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]