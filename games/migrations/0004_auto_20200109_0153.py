# Generated by Django 2.2.7 on 2020-01-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20200109_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(),
        ),
    ]
