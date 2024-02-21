from django.db import models


class PartTimeJob(models.TextChoices):
    FULL_TIME = "FULL_TIME", "To'liq bandlik"
    NIGHT = "NIGHT", "Kechqurun"
    ON_WEEKENDS = "ON_WEEKENDS", "Dam olish kunlari"
    HALF_DAY = "HALF_DAY", "Yarim kunlik"
    ONE = "ONE", "Bir martalik"


class DEGREE(models.TextChoices):
    ONE_TO_THREE = "ONE_TO_THREE", "1 yildan 3 yilgacha"
    THREE_TO_FIVE = "THREE_TO_FIVE", "3 yildan 6 yilgacha"
    NO_DEGREE = "NO_DEGREE", "Tajriba yo'q"


class BANDLIK(models.TextChoices):
    FULL_TIME = "FULL_TIME", "To'liq vaqt"
    YARIM = "YARIM", "Yarim kunlik"
    AMALIYOT = "AMALIYOT", "AMALIYOT"
    LOYIHA = "LOYIHA", "Loyiha ishi"


class IshGRAFIGI(models.TextChoices):
    FULL = "FULL", "To'liq kun"
    SHIFT = "SHIFT", "shift jadvali"
    MOSLASHUVCHAN = "MOSLASHUVCHAN", "Moslashuvchan"
    MASOFAVIY = "MASOFAVIY", "Masofaviy"


class EDU(models.TextChoices):
    NULL = "NULL", "Majburiy emas yoki ko'rsatilmagan"
    TOP = "TOP", "Oliy"
    SPECIAL = "SHIFT", "O'rta maxsus"
