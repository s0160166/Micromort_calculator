# Generated by Django 4.1.4 on 2022-12-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_info_hobby'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='alcogol',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='cigarets',
            field=models.IntegerField(default=0),
        ),
    ]
