# Generated by Django 4.1 on 2023-05-08 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tags", "0001_initial"),
        ("events", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("venues", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="followers",
            field=models.ManyToManyField(
                blank=True, related_name="following_event", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="event", to="tags.tags"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="venue",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event",
                to="venues.venue",
            ),
        ),
    ]
