# Generated by Django 4.0.4 on 2022-08-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.IntegerField(max_length=7)),
                ('house', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
            ],
        ),
    ]
