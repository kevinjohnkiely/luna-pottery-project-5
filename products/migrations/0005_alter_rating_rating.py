# Generated by Django 3.2 on 2022-09-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
    ]
