# Generated by Django 2.1.7 on 2019-05-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20190523_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgposttag',
            name='img_tag',
        ),
        migrations.AddField(
            model_name='imgpost',
            name='img_tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='main.ImgPostTag'),
        ),
        migrations.AlterField(
            model_name='imgposttag',
            name='tag_name',
            field=models.SlugField(),
        ),
    ]