# Generated by Django 4.1.4 on 2022-12-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_info_alcogol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='profession',
            field=models.CharField(choices=[('0', 'Работа в офисе/на дому/работа, не связанная с риском'), ('0.726027397260274', 'Пилот'), ('0.5945205479452055', 'Рыбак'), ('0.5616438356164384', 'Водитель грузового транспорта'), ('0.4712328767123288', 'Лесоруб'), ('0.4520547945205479', 'Строитель'), ('0.4383561643835616', 'Моряк'), ('0.3863013698630137', 'Литейшик'), ('0.38082191780821917', 'Рабочий деревообрабатывающей промышленности'), ('0.3232876712328767', 'Шахтёр'), ('0.29315068493150687', 'Фермер')], default=0, max_length=50),
        ),
    ]