# Generated by Django 2.1.11 on 2020-01-21 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='user',
        ),
    ]
