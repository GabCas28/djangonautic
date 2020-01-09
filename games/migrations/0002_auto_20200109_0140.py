# Generated by Django 2.2.7 on 2020-01-08 23:40

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'])),
        ),
    ]
