# Generated by Django 3.0.2 on 2020-01-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='dob',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='mobile',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='p2mob',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='information',
            name='pmob',
            field=models.IntegerField(max_length=100),
        ),
    ]
