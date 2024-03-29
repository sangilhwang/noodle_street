# Generated by Django 5.0.2 on 2024-02-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "single_pages",
            "0009_alter_restraunt_address_alter_restraunt_address_gu_and_more",
        ),
        ("users", "0004_alter_user_birthday"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="like_posts",
            field=models.ManyToManyField(
                blank=True,
                related_name="like_users",
                to="single_pages.restraunt",
                verbose_name="좋아요 누른 Restaurant 목록",
            ),
        ),
    ]
