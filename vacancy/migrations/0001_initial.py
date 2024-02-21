# Generated by Django 4.2.7 on 2024-02-20 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("slug", models.SlugField(max_length=128, verbose_name="self")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="vacancy.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MasterType",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="categories", to="vacancy.category"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Search",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("update_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("company", models.CharField(max_length=128)),
                ("from_price", models.IntegerField(blank=True, null=True)),
                ("to_price", models.IntegerField(blank=True, null=True)),
                ("is_position", models.BooleanField(default=True)),
                ("is_company", models.BooleanField(default=True)),
                ("is_job", models.BooleanField(default=True)),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("1 yildan 3 yilgacha", "One To Three"),
                            ("3 yildan 6 yilgacha", "Three To Five"),
                            ("Tajriba yo'q", "No Degree"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "bandlik",
                    models.CharField(
                        choices=[
                            ("To'liq vaqt", "Full Time"),
                            ("Yarim kunlik", "Yarim"),
                            ("AMALIYOT", "Amaliyot"),
                            ("Loyiha ishi", "Loyiha"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "part_time",
                    models.CharField(
                        choices=[
                            ("To'liq bandlik", "Full Time"),
                            ("Kechqurun", "Night"),
                            ("Dam olish kunlari", "On Weekends"),
                            ("Yarim kunlik", "Half Day"),
                            ("Bir martalik", "One"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "grafik",
                    models.CharField(
                        choices=[
                            ("To'liq kun", "Full"),
                            ("shift jadvali", "Shift"),
                            ("Moslashuvchan", "Moslashuvchan"),
                            ("Masofaviy", "Masofaviy"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "edu",
                    models.CharField(
                        choices=[
                            ("Majburiy emas yoki ko'rsatilmagan", "Null"),
                            ("Oliy", "Top"),
                            ("O'rta maxsus", "Special"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="district",
                        to="vacancy.district",
                    ),
                ),
                (
                    "master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="master", to="vacancy.mastertype"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="region", to="vacancy.region"
                    ),
                ),
                ("skills", models.ManyToManyField(related_name="skills", to="vacancy.skills")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="district",
            name="region",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="vacancy.region"),
        ),
    ]