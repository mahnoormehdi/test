# Generated by Django 5.0 on 2023-12-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=60)),
                ('province', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
