from django.urls import path
from daApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detailed-today', views.detailedToday, name='detailedToday'),
    path('expense-on-a-date', views.expenseOnADate, name='expenseOnADate'),
    path('expense-on-a-month', views.expenseOnAMonth, name='expenseOnAMonth'),
    path('total-expense-in-a-day', views.totalExpenseInADay, name='totalExpenseInADay'),
    path('total-expense-in-a-month', views.totalExpenseInAMonth, name='totalExpenseInAMonth'),
]