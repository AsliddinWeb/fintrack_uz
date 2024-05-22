from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

# Local
from account_app.models import Account
from .models import Income
from .serializers import IncomeSerializer

class IncomeListCreateView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        account = Account.objects.get(user=user)
        serializer.save(user=user, account=account)
        income = serializer.instance
        account.balance += income.amount
        account.save()

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
