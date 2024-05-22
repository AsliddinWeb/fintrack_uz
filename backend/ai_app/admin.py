from django.contrib import admin
from .models import FinancialAdvice

@admin.register(FinancialAdvice)
class FinancialAdviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'advice', 'created_at')
    search_fields = ('user__username', 'question', 'advice')
    list_filter = ('created_at', 'user')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('user', 'question', 'advice')
        }),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)