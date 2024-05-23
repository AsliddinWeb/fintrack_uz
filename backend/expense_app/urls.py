from django.urls import path
from .views import ExpenseListCreateView, ExpenseDetailView, ExpenseCaetgoryList

urlpatterns = [
    path('', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),

    path('categories/', ExpenseCaetgoryList.as_view(), name='expense-category-list'),


]
