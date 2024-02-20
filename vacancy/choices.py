from django.db import models


class PartTimeJob(models.TextChoices):
    FULL_TIME = "To'liq bandlik"
    NIGHT = "Kechqurun"
    ON_WEEKENDS = "Dam olish kunlari"
    HALF_DAY = "Yarim kunlik"
    ONE = "Bir martalik"


class DEGREE(models.TextChoices):
    ONE_TO_THREE = "1 yildan 3 yilgacha"
    THREE_TO_FIVE = "3 yildan 6 yilgacha"
    NO_DEGREE = "Tajriba yo'q"


class BANDLIK(models.TextChoices):
    FULL_TIME = "To'liq vaqt"
    YARIM = "Yarim kunlik"
    AMALIYOT = "AMALIYOT"
    LOYIHA = "Loyiha ishi"


class IshGRAFIGI(models.TextChoices):
    FULL = "To'liq kun"
    SHIFT = "shift jadvali"
    MOSLASHUVCHAN = "Moslashuvchan"
    MASOFAVIY = "Masofaviy"


class EDU(models.TextChoices):
    NULL = "Majburiy emas yoki ko'rsatilmagan"
    TOP = "Oliy"
    SPECIAL = "O'rta maxsus"
