from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Income

@receiver(post_save, sender=Income)
def update_account_balance_on_income(sender, instance, created, **kwargs):
    if created:
        account = instance.account
        account.balance += instance.amount
        account.save()

@receiver(pre_delete, sender=Income)
def revert_account_balance_on_income_delete(sender, instance, **kwargs):
    account = instance.account
    account.balance -= instance.amount
    account.save()
