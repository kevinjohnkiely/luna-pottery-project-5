# Generated by Django 3.2 on 2022-09-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20220916_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avg_rating',
            new_name='rating',
        ),
    ]
