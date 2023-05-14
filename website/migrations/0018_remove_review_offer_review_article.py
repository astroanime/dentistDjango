# Generated by Django 4.1.6 on 2023-05-13 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_article_a_link"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="offer",
        ),
        migrations.AddField(
            model_name="review",
            name="article",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="website.article",
            ),
        ),
    ]
