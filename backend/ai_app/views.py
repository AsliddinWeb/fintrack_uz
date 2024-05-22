from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import FinancialAdviceSerializer
from .ai_service import get_financial_advice
from .models import FinancialAdvice

class FinancialAdviceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FinancialAdviceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            question = serializer.validated_data['question']
            advice = get_financial_advice(question)
            FinancialAdvice.objects.create(
                user=request.user,
                question=question,
                advice=advice
            )
            return Response({"question": question, "advice": advice}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
