# Generated by Django 4.1.3 on 2022-11-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference', models.CharField(max_length=30)),
                ('trademark', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=4)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=150)),
                ('supplier', models.CharField(max_length=60)),
            ],
        ),
    ]
