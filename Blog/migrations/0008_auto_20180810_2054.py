# Generated by Django 2.0.5 on 2018-08-10 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20180810_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='oowner',
            new_name='owner',
        ),
    ]
