# Generated by Django 4.2.16 on 2024-12-27 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_login',
            old_name='uname',
            new_name='lname',
        ),
    ]
