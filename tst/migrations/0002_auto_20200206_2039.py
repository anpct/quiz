# Generated by Django 3.0.3 on 2020-02-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resp',
            name='resp',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
