# Generated by Django 3.1 on 2020-08-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0002_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
