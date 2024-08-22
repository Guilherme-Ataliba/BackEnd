# Generated by Django 5.1 on 2024-08-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fotografia",
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
                ("name", models.CharField(max_length=100)),
                ("legenda", models.CharField(max_length=150)),
                ("descricao", models.TextField()),
                ("foto", models.CharField(max_length=100)),
            ],
        ),
    ]
