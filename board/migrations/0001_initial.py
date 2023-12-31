# Generated by Django 4.2.2 on 2023-06-26 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardTB",
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
                (
                    "brd_id",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="board ID"
                    ),
                ),
                (
                    "brd_title",
                    models.CharField(max_length=200, verbose_name="board title"),
                ),
                ("brd_content", models.TextField(verbose_name="board content")),
                ("brd_create", models.DateTimeField(auto_now_add=True)),
                ("brd_update", models.DateTimeField(auto_now=True)),
                (
                    "usr_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
