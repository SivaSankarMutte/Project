# Generated by Django 3.0 on 2021-07-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0006_auto_20210708_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uimg',
            field=models.ImageField(default='dummyProfile.png', upload_to='Profilepics/'),
        ),
    ]
