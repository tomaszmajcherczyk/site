# Generated by Django 2.1.7 on 2019-05-28 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20190528_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgpost',
            old_name='img_tag',
            new_name='img_tags',
        ),
    ]
