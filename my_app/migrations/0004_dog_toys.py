# Generated by Django 5.1.2 on 2024-10-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_toy_alter_feeding_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='my_app.toy'),
        ),
    ]