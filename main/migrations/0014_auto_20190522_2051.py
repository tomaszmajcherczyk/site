# Generated by Django 2.1.7 on 2019-05-22 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190522_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgpost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
