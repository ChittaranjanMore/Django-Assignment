# Generated by Django 3.0 on 2021-06-17 14:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_educationaldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='LongDecription',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='educationaldetails',
            name='CertificateImage',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)]),
        ),
    ]