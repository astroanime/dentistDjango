# Generated by Django 4.1.6 on 2023-05-11 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "website",
            "0007_remove_appointment_service_remove_appointment_stuff_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="Language",
        ),
        migrations.DeleteModel(
            name="Programmer",
        ),
    ]
