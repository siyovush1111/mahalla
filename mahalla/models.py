from django.db import models
from django.contrib.auth.models import User


class Sector(models.Model):
    name = models.CharField(verbose_name="sektor nomi", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sektor"
        ordering = ("id",)


class Neighborhood(models.Model):
    sector = models.ForeignKey('sector', on_delete=models.PROTECT,
                               help_text="Mahalla qaysi sektorga tegishli ekanligini tanlang")
    name = models.CharField(verbose_name="mahalla nomi ", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahalalar"
        ordering = ("id",)


class Citizen(models.Model):
    GENDER = (
        ("male", "erkak"),
        ("female", "ayol"),
    )
    EDUCATED = (
        ("middle", "o'rta ma'lumotli"),
        ("senior", "oliy malumotli"),
    )
    IRON_NOTE = (
        ("yes", "ha"),
        ("no", "yo'q")
    )
    ABROAD = (
        ("yes", "ha"),
        ("no", "yo'q"),
    )
    DISABILLITY = (
        ("yes", "ha"),
        ("no", "yo'q")
    )
    WOMEN_NOTE = (
        ("yes", "ha"),
        ("no", "yo'q")
    )
    neighborhood = models.ForeignKey("neighborhood", verbose_name="mahallani tanlang",
                                     on_delete=models.PROTECT)
    full_name = models.CharField(verbose_name="F.I.O", max_length=25)
    passport = models.CharField(verbose_name="Passport seriyasi", max_length=20)
    birthdate = models.DateField(verbose_name="tug'ilgan sanasi")
    gender = models.CharField(
        max_length=250,
        choices=GENDER,
        verbose_name="Fuqoro jinsi",
    )
    educated = models.CharField(
        verbose_name="Fuqoro ma'lumoti",
        choices=EDUCATED,
        max_length=250
    )
    adress = models.TextField(verbose_name="yashash manzili")

    iron_note = models.CharField(
        verbose_name="Temir daftarga kiritilganmi?",
        max_length=250,
        choices=IRON_NOTE
    )
    abroad = models.CharField(
        verbose_name="Chet eldami",
        max_length=250,
        choices=ABROAD,

    )
    disabillity = models.CharField(
        verbose_name="Nogironligi bormi?",
        max_length=20,
        choices=DISABILLITY,
    )
    women_note = models.CharField(
        max_length=250,
        verbose_name="Ayollar daftariga kiritilganmi?",
        choices=WOMEN_NOTE
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Fuqoro"
        verbose_name_plural = "Fuqorolar"
        ordering = ("id",)
