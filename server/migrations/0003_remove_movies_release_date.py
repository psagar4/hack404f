# Generated by Django 2.0.5 on 2018-05-10 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20180510_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='release_date',
        ),
    ]
