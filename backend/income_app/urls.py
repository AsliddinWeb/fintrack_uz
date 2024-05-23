from django.urls import path
from .views import IncomeListCreateView, IncomeDetailView, IncomeCaetgoryList

urlpatterns = [
    path('', IncomeListCreateView.as_view(), name='income-list-create'),
    path('<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),

    path('categories/', IncomeCaetgoryList.as_view(), name='income-category-list'),
]
