from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    account = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'user', 'account', 'category', 'amount', 'description', 'date']
