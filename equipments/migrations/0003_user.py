# Generated by Django 2.0.5 on 2018-08-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_auto_20180520_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]