# Generated by Django 5.1.1 on 2024-10-02 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_alumni_year_graduated'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredAlumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='college',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='district',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='program',
        ),
        migrations.AlterField(
            model_name='alumni',
            name='year_graduated',
            field=models.IntegerField(choices=[(2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')]),
        ),
    ]
