# Generated by Django 4.1 on 2022-08-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parcel_management_app", "0005_parcel_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parcel",
            name="code",
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
