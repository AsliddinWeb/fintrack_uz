from django.db import models
from django.contrib.auth.models import User

# Hisob (Account) modeli
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi", related_name='account')
    name = models.CharField(max_length=100, verbose_name="Hisob Nomi")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Balans")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hisob"
        verbose_name_plural = "Hisoblar"