# Generated by Django 3.1.4 on 2020-12-24 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_remove_userinfo_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='profile_icon',
        ),
    ]
