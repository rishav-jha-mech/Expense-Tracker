from django import template

from daApp.models import Expense

register = template.Library()

@register.filter
def totalExpense(expenses):
    return sum([expense.amount for expense in expenses])