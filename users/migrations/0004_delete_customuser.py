# Generated by Django 3.0.6 on 2020-11-11 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
