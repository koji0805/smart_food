# Generated by Django 4.1 on 2024-03-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Foods",
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
                ("create_at", models.DateTimeField()),
                ("update_at", models.DateTimeField()),
                ("name", models.CharField(max_length=255)),
                ("expirydate", models.DateField()),
                ("quantity", models.IntegerField()),
            ],
            options={
                "db_table": "foods",
            },
        ),
    ]
