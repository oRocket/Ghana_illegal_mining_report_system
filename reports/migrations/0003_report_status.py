# Generated by Django 5.1.1 on 2024-10-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
