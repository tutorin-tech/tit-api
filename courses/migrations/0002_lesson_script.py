# Generated by Django 3.2 on 2021-05-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='script',
            field=models.TextField(default=''),
        ),
    ]
