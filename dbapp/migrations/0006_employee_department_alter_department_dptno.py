# Generated by Django 5.0.1 on 2024-02-09 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0005_remove_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dbapp.department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='dptno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]