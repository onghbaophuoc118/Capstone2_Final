# Generated by Django 3.0.10 on 2020-11-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_directinginfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='directinginfo',
            name='dictrict',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]