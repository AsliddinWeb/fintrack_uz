from rest_framework import serializers
from .models import Income, IncomeCategory

class IncomeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    account = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Income
        fields = ['id', 'user', 'account', 'category', 'amount', 'description', 'date']

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = "__all__"