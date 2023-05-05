# Generated by Django 4.1 on 2023-05-02 16:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=80)),
                ("summary", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(blank=True)),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("changed", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "draft"),
                            ("live", "live"),
                            ("started", "started"),
                            ("ended", "ended"),
                            ("completed", "completed"),
                            ("canceled", "canceled"),
                        ],
                        default="draft",
                        max_length=16,
                    ),
                ),
                ("online_event", models.BooleanField()),
                ("hide_start_date", models.BooleanField()),
                ("hide_end_date", models.BooleanField()),
                ("free", models.BooleanField(default=False)),
                ("waitlist", models.BooleanField(default=False)),
                (
                    "view_counter",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("age_restriction", models.BooleanField(default=False)),
                ("fully_booked", models.BooleanField(default=False)),
                ("published", models.BooleanField(default=False)),
                ("organizer", models.CharField(max_length=80)),
                ("video_url", models.URLField(blank=True)),
                ("timezone", models.CharField(max_length=10)),
                ("language", models.CharField(max_length=20)),
                ("listed", models.BooleanField(default=True)),
                ("shareable", models.BooleanField(default=True)),
                ("invite_only", models.BooleanField(default=False)),
                ("show_remaining", models.BooleanField(default=False)),
                ("password", models.TextField(null=True)),
                ("capacity", models.IntegerField(default=50)),
                ("capacity_is_custom", models.BooleanField(default=False)),
                (
                    "category",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="event",
                        to="categories.categories",
                    ),
                ),
            ],
        ),
    ]
