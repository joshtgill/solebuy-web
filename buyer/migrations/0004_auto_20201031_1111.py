# Generated by Django 3.1.2 on 2020-10-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_auto_20201031_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assisterfilterid',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='products',
            field=models.ManyToManyField(to='buyer.AssisterFilterId'),
        ),
    ]