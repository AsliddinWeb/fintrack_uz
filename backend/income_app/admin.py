from django.contrib import admin
from .models import IncomeCategory, Income

@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'account', 'category', 'amount', 'date')
    search_fields = ('user__username', 'account__name', 'category__name')
    list_filter = ('category', 'date')