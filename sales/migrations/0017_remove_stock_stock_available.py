# Generated by Django 3.0.6 on 2020-05-26 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0016_stock_stock_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='stock_available',
        ),
    ]
