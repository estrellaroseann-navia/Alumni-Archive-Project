# Generated by Django 5.1.1 on 2024-09-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_alumni_yeargraduated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='yearGraduated',
        ),
        migrations.AddField(
            model_name='alumni',
            name='year_graduated',
            field=models.IntegerField(choices=[(2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=0),
        ),
    ]
