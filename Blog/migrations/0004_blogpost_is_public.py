# Generated by Django 2.0.5 on 2018-07-13 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogpost_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
