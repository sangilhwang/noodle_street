# Generated by Django 4.1 on 2024-02-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_birthday_alter_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(null=True, verbose_name="생년월일"),
        ),
    ]