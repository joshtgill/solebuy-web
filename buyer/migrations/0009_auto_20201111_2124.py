# Generated by Django 3.1.2 on 2020-11-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0008_auto_20201111_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='displayDescription',
            field=models.CharField(default='', max_length=50),
        ),
    ]
