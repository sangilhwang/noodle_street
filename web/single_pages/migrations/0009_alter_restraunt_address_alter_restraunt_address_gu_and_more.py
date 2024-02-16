# Generated by Django 4.1 on 2024-02-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("single_pages", "0008_alter_restraunt_phone_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restraunt",
            name="address",
            field=models.CharField(max_length=30, null=True, verbose_name="주소"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="address_gu",
            field=models.CharField(max_length=5, null=True, verbose_name="구"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="image",
            field=models.ImageField(null=True, upload_to=None, verbose_name="대표 이미지"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="name",
            field=models.CharField(max_length=30, null=True, verbose_name="이름"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="rating",
            field=models.FloatField(null=True, verbose_name="평점"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="rating_count",
            field=models.IntegerField(null=True, verbose_name="평점 수"),
        ),
    ]
