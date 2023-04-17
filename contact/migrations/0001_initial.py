# Generated by Django 3.1.14 on 2023-03-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('massage', models.TextField()),
            ],
        ),
    ]
