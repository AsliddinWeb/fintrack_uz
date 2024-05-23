from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

# Filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import IncomeFilter

# Local
from account_app.models import Account
from .models import Income, IncomeCategory
from .serializers import IncomeSerializer, IncomeCategorySerializer

class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = IncomeFilter

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        account = Account.objects.get(user=user)
        serializer.save(user=user, account=account)
        income = serializer.instance
        account.balance += income.amount
        account.save()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_schema_fields(self, view):
        extra_fields = []
        for backend in list(self.filter_backends):
            if hasattr(backend(), 'get_schema_fields'):
                extra_fields += backend().get_schema_fields(view)
        return extra_fields

class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_update(self, serializer):
        instance = self.get_object()
        previous_amount = instance.amount
        income = serializer.save()
        account = income.account
        account.balance += income.amount - previous_amount
        account.save()


class IncomeCaetgoryList(generics.ListAPIView):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer