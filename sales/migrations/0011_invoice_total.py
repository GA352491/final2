# Generated by Django 3.0.6 on 2020-05-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0010_remove_invoice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
