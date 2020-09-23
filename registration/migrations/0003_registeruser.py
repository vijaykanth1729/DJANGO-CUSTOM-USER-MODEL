# Generated by Django 3.1.1 on 2020-09-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200923_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
