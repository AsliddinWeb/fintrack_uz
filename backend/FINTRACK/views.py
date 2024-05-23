from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from django.db.models import Sum
from datetime import timedelta


from expense_app.models import Expense
from income_app.models import Income

import calendar

class DataView(APIView):
    permission_classes = [IsAuthenticated]

    def get_data(self, user, start_date, end_date):
        expenses = Expense.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
        incomes = Income.objects.filter(user=user, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
        return {'expenses': expenses, 'incomes': incomes}

    def get_daily_data(self, user):
        start_date = now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = now().replace(hour=23, minute=59, second=59, microsecond=999999)
        data = [self.get_data(user, start_date, end_date)]
        labels = [start_date.strftime('%Y-%m-%d')]
        return labels, data

    def get_weekly_data(self, user):
        start_date = now() - timedelta(days=now().weekday())
        end_date = start_date + timedelta(days=6)
        data = [self.get_data(user, start_date + timedelta(days=i), start_date + timedelta(days=i)) for i in range(7)]
        labels = [(start_date + timedelta(days=i)).strftime('%A') for i in range(7)]
        labels = [self.translate_day(label) for label in labels]
        return labels, data

    def get_monthly_data(self, user):
        start_date = now().replace(day=1)
        end_date = (now().replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        data = []
        labels = []
        current_date = start_date
        while current_date <= end_date:
            day_end = current_date + timedelta(days=1) - timedelta(seconds=1)
            data.append(self.get_data(user, current_date, day_end))
            labels.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
        return labels, data

    def get_yearly_data(self, user):
        start_date = now().replace(month=1, day=1)
        end_date = now().replace(month=12, day=31)
        data = []
        labels = []
        for month in range(1, 13):
            month_start = start_date.replace(month=month)
            month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            data.append(self.get_data(user, month_start, month_end))
            labels.append(calendar.month_name[month])
        labels = [self.translate_month(label) for label in labels]
        return labels, data

    def translate_day(self, day):
        days = {
            "Monday": "Dushanba",
            "Tuesday": "Seshanba",
            "Wednesday": "Chorshanba",
            "Thursday": "Payshanba",
            "Friday": "Juma",
            "Saturday": "Shanba",
            "Sunday": "Yakshanba"
        }
        return days.get(day, day)

    def translate_month(self, month):
        months = {
            "January": "Yanvar",
            "February": "Fevral",
            "March": "Mart",
            "April": "Aprel",
            "May": "May",
            "June": "Iyun",
            "July": "Iyul",
            "August": "Avgust",
            "September": "Sentabr",
            "October": "Oktabr",
            "November": "Noyabr",
            "December": "Dekabr"
        }
        return months.get(month, month)

    def get(self, request, period, format=None):
        user = request.user

        if period == 'daily':
            labels, data = self.get_daily_data(user)
        elif period == 'weekly':
            labels, data = self.get_weekly_data(user)
        elif period == 'monthly':
            labels, data = self.get_monthly_data(user)
        elif period == 'yearly':
            labels, data = self.get_yearly_data(user)
        else:
            return Response({"error": "Invalid period specified"}, status=400)

        response_data = {
            "labels": labels,
            "incomes": [entry['incomes'] for entry in data],
            "expenses": [entry['expenses'] for entry in data]
        }
        return Response(response_data)
