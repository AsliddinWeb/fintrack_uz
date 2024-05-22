from django.urls import path
from .views import FinancialAdviceView

urlpatterns = [
    path('', FinancialAdviceView.as_view(), name='financial-advice'),
]
