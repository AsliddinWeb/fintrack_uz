from django.db import models
from django.contrib.auth.models import User
from account_app.models import Account

# Harajat Kategoriya modeli
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Harajat Kategoriyasi"
        verbose_name_plural = "Harajat Kategoriyalari"

# Harajat modeli
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Hisob")
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Miqdor")
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name="Tavsif")
    date = models.DateTimeField(verbose_name="Sana")

    def __str__(self):
        return f"Expense - {self.amount} - {self.date}"

    class Meta:
        verbose_name = "Harajat"
        verbose_name_plural = "Harajatlar"
