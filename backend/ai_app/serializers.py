from rest_framework import serializers
from .models import FinancialAdvice

class FinancialAdviceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FinancialAdvice
        fields = ['user', 'question', 'advice']
        read_only_fields = ['advice']
