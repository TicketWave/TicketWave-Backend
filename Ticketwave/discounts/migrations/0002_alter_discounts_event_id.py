# Generated by Django 4.1.7 on 2023-03-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discounts',
            name='event_id',
            field=models.IntegerField(default=-1),
        ),
    ]
