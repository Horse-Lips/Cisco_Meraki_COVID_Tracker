# Generated by Django 3.1.2 on 2021-02-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210210_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapshot',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
