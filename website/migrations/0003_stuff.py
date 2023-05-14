# Generated by Django 3.0.2 on 2020-11-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_field_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('emails', models.CharField(max_length=200, null=True)),
                ('date_created', models.TimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
