# Generated by Django 4.2.2 on 2023-07-04 10:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("construction", "0010_remove_constructiontb_cstr_manager_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="constructioncalltb",
            name="cstr_desc",
        ),
    ]
