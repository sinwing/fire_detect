# Generated by Django 2.2.4 on 2019-08-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fireoffice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('headoffice', models.CharField(max_length=45)),
                ('fireoffice', models.CharField(max_length=45)),
                ('center', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]
