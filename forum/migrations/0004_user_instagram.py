# Generated by Django 5.0.2 on 2024-03-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_user_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="instagram",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
