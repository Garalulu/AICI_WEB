# Generated by Django 4.2.2 on 2023-07-03 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("construction", "0008_alter_constructiontb_receipt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="constructiontb",
            name="receipt",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date added"
            ),
        ),
    ]
