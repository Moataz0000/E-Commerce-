# Generated by Django 3.2.3 on 2024-04-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Rejection', 'Rejection'), ('Processing', 'Processing'), ('Shipping', 'Shipping')], default=('Processing', 'Processing'), max_length=50),
        ),
    ]
