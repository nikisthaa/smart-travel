# Generated by Django 2.0.7 on 2018-08-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Query', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restdetail',
            name='Desc',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='restdetail',
            name='P_Name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='restdetail',
            name='Popular_for',
            field=models.CharField(max_length=1000),
        ),
    ]
