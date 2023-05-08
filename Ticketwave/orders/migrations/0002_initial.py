# Generated by Django 4.1 on 2023-05-08 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orders", "0001_initial"),
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="ticket",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order",
                to="tickets.ticket",
            ),
        ),
    ]
