# Generated by Django 3.0.3 on 2020-08-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Quantity', models.IntegerField()),
                ('ImgSrc', models.CharField(max_length=50)),
            ],
        ),
    ]
