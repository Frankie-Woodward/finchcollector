# Generated by Django 4.2.6 on 2023-10-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('battery_mileage', models.IntegerField()),
            ],
        ),
    ]