# Generated by Django 4.2.7 on 2023-11-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_app", "0003_profitandloss"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="productImage",
        ),
        migrations.AlterField(
            model_name="product",
            name="productCode",
            field=models.IntegerField(),
        ),
    ]
