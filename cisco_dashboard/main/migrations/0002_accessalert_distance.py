# Generated by Django 3.1.2 on 2021-03-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessalert',
            name='distance',
            field=models.CharField(default=0.1, max_length=10),
            preserve_default=False,
        ),
    ]
