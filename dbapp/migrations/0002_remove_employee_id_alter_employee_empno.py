# Generated by Django 5.0.1 on 2024-02-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='empno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]