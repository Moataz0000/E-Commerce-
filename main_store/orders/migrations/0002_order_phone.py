# Generated by Django 3.2.3 on 2024-02-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
