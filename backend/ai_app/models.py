from django.db import models
from django.contrib.auth.models import User

class FinancialAdvice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    question = models.CharField(max_length=600, verbose_name="Savol")
    advice = models.TextField(verbose_name="Javob", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Moliyaviy Maslahat"
        verbose_name_plural = "Moliyaviy Maslahatlar"
