# Generated by Django 4.1 on 2024-03-27 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pictures",
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
                ("picture", models.FileField(upload_to="picture/")),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="food.foods"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]