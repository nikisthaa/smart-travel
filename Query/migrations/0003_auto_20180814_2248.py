# Generated by Django 2.0.7 on 2018-08-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0002_auto_20180813_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedetail',
            name='Entry_fee',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
