# Generated by Django 5.1.1 on 2024-10-19 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_blogpost_image_link_report_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='report',
            name='image_link',
        ),
    ]
