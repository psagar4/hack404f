# Generated by Django 2.0.5 on 2018-05-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_remove_movies_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credits',
            name='credit_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
