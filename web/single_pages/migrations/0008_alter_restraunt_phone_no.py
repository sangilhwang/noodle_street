# Generated by Django 4.1 on 2024-02-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("single_pages", "0007_alter_restraunt_fri_break_end_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restraunt",
            name="phone_no",
            field=models.CharField(max_length=15, null=True, verbose_name="연락처"),
        ),
    ]