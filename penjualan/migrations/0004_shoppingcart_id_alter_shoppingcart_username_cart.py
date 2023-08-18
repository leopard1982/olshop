# Generated by Django 4.2.3 on 2023-08-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penjualan', '0003_remove_shoppingcart_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='username_cart',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
