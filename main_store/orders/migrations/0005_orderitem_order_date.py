# Generated by Django 3.2.3 on 2024-03-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]
