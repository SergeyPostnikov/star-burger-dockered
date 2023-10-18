# Generated by Django 3.2.15 on 2023-10-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0062_alter_order_cooking_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('CARD', 'Картой'), ('CASH', 'Наличные')], db_index=True, max_length=6, verbose_name='метод оплаты'),
        ),
    ]
