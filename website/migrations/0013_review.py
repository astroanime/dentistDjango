# Generated by Django 4.1.6 on 2023-05-11 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("website", "0012_offer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(help_text="The Review text.")),
                (
                    "rating",
                    models.IntegerField(help_text="The the reviewer has given."),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time the review was created.",
                    ),
                ),
                (
                    "date_edited",
                    models.DateTimeField(
                        help_text="The date and time the review was last edited.",
                        null=True,
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="website.offer"
                    ),
                ),
            ],
        ),
    ]