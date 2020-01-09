# Generated by Django 2.2.7 on 2020-01-08 19:21

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(blank=True)),
                ('price', models.FloatField(default=0.0)),
                ('high_scores', jsonfield.fields.JSONField(default={'first': 0.0, 'second': 0.0, 'third': 0.0})),
            ],
        ),
    ]
