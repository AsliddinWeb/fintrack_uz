from django.db import models
from django.contrib.auth.models import User
from account_app.models import Account

# Daromad Kategoriya modeli
class IncomeCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Daromad Kategoriyasi"
        verbose_name_plural = "Daromad Kategoriyalari"

# Daromad modeli
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Hisob")
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdor")
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tavsif")
    date = models.DateField(verbose_name="Sana")

    def __str__(self):
        return f"Income - {self.amount} - {self.date}"

    class Meta:
        verbose_name = "Daromad"
        verbose_name_plural = "Daromadlar"