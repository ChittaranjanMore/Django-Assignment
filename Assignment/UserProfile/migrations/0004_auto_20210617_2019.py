# Generated by Django 3.0 on 2021-06-17 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_auto_20210617_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='LongDecription',
            new_name='LongDescription',
        ),
    ]
