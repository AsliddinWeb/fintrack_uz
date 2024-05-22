from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Expense

@receiver(post_save, sender=Expense)
def update_account_balance_on_expense(sender, instance, created, **kwargs):
    if created:
        account = instance.account
        account.balance -= instance.amount
        account.save()

@receiver(pre_delete, sender=Expense)
def revert_account_balance_on_expense_delete(sender, instance, **kwargs):
    account = instance.account
    account.balance += instance.amount
    account.save()