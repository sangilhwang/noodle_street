# Generated by Django 5.0.2 on 2024-02-19 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_like_posts"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="like_posts",
            new_name="like_restaurants",
        ),
    ]
