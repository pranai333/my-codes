# Generated by Django 5.0.1 on 2024-02-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0020_cars_drivers'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='images',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
