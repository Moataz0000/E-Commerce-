# Generated by Django 3.2.3 on 2024-04-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_remove_orderitem_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]