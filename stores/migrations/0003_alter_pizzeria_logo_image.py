# Generated by Django 3.2.8 on 2021-10-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_alter_pizzeria_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='logo_image',
            field=models.ImageField(blank=True, upload_to='pizzaImages'),
        ),
    ]