# Generated by Django 3.0 on 2021-07-18 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]