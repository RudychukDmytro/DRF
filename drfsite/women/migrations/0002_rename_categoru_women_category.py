# Generated by Django 4.2.3 on 2023-07-07 18:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("women", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="women",
            old_name="categoru",
            new_name="category",
        ),
    ]
