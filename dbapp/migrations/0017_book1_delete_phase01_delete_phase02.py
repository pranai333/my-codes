# Generated by Django 5.0.1 on 2024-02-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0016_rename_base01_phase01_rename_base02_phase02'),
    ]

    operations = [
        migrations.CreateModel(
            name='book1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookno', models.IntegerField()),
                ('bookname', models.CharField(max_length=20)),
                ('bookauthor', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='phase01',
        ),
        migrations.DeleteModel(
            name='phase02',
        ),
    ]