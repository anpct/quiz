# Generated by Django 3.0.3 on 2020-02-11 16:06

from django.conf import settings
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passkey', models.CharField(max_length=6, validators=[user.models.validate_key])),
                ('resp', models.CharField(blank=True, max_length=30, null=True)),
                ('roll_no', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]