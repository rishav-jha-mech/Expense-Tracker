from django.contrib import admin
from daApp.models import Expense, Balance


class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ('date','amount','person','category','description')

admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Balance)