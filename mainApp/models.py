from tkinter.constants import CASCADE

from django.db import models
from django.db.models import SET_NULL


class Yonalish(models.Model):

    nomi = models.CharField(max_length=100)
    aktiv = models.BooleanField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Yo'nalishlar"

class Fan(models.Model):
    nomi = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Fanlar"

class   Ustoz(models.Model):
    jins_choices = (
        ('Erkak','Erkak'),
        ('Ayol','Ayol')
    )
    daraja_choices = (
        ('Bakalavr','Bakalavr'),
        ('Magistr','Magistr'),
        ("Dotsent", "Dotsent")
    )
    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10 , choices=jins_choices)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=100, choices=daraja_choices)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = "Ustozlar"