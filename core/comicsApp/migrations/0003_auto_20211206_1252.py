# Generated by Django 3.2.9 on 2021-12-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicsApp', '0002_auto_20211204_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='thumbnail',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterModelTable(
            name='character',
            table='character',
        ),
    ]