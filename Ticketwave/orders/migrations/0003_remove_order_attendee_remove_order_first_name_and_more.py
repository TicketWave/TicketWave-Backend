# Generated by Django 4.1 on 2023-05-10 00:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="attendee",
        ),
        migrations.RemoveField(
            model_name="order",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="last_name",
        ),
    ]