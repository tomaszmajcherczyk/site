# Generated by Django 2.1.7 on 2019-05-20 06:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190517_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='imgpost',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 20, 6, 50, 0, 278243, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='imgpost',
            name='site_users',
            field=models.ManyToManyField(to='main.SiteUser'),
        ),
    ]
