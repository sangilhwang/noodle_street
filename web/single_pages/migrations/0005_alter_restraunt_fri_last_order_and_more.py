# Generated by Django 5.0.2 on 2024-02-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "single_pages",
            "0004_alter_restraunt_fri_start_alter_restraunt_mon_start_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="restraunt",
            name="fri_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="금요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="mon_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="월요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="sat_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="토요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="sun_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="일요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="thu_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="목요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="tue_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="화요일 주문 마감"),
        ),
        migrations.AlterField(
            model_name="restraunt",
            name="wed_last_order",
            field=models.CharField(max_length=20, null=True, verbose_name="수요일 주문 마감"),
        ),
    ]
