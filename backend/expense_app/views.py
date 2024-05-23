from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

# Filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ExpenseFilter

# Local
from account_app.models import Account
from .models import Expense, ExpenseCategory
from .serializers import ExpenseSerializer, ExpenseCategorySerializer

class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        account = Account.objects.get(user=user)
        serializer.save(user=user, account=account)
        expense = serializer.instance
        account.balance -= expense.amount
        account.save()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_schema_fields(self, view):
        extra_fields = []
        for backend in list(self.filter_backends):
            if hasattr(backend(), 'get_schema_fields'):
                extra_fields += backend().get_schema_fields(view)
        return extra_fields

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_update(self, serializer):
        instance = self.get_object()
        previous_amount = instance.amount
        expense = serializer.save()
        account = expense.account
        account.balance += previous_amount - expense.amount
        account.save()


class ExpenseCaetgoryList(generics.ListAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer