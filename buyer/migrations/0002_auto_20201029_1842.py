# Generated by Django 3.1.2 on 2020-10-29 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='iconPath',
            new_name='iconFileName',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='imagePath',
            new_name='imageFileName',
        ),
    ]
