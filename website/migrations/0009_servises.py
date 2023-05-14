# Generated by Django 4.1.6 on 2023-05-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0008_delete_language_delete_programmer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Servises",
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
                ("name", models.CharField(default=None, max_length=40)),
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField(default=10)),
            ],
        ),
    ]
