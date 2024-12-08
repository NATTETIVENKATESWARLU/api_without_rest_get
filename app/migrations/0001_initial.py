# Generated by Django 5.1.3 on 2024-11-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="employees",
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
                ("eno", models.IntegerField()),
                ("ename", models.CharField(max_length=200)),
                ("esal", models.IntegerField()),
                ("eaddress", models.CharField(max_length=200)),
            ],
        ),
    ]