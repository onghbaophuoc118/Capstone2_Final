# Generated by Django 3.0.10 on 2020-12-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_patientinfo_id_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
