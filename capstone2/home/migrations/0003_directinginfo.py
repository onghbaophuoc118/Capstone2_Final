# Generated by Django 3.0.10 on 2020-11-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=500)),
                ('effect', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
