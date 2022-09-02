from django.urls import path
from daApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detailed-today', views.detailedToday, name='detailedToday'),
    path('daily-report', views.dailyReport, name='dailyReport'),
    path('monthly-report', views.monthlyReport, name='monthlyReport'),
    path('expense-on-a-date/<slug:slug>', views.expenseOnADate, name='expenseOnADate'),
    path('expense-on-a-month', views.expenseOnAMonth, name='expenseOnAMonth'),
    path('total-expense-in-a-day/<slug:slug>', views.totalExpenseInADay, name='totalExpenseInADay'),
    path('total-expense-in-a-month', views.totalExpenseInAMonth, name='totalExpenseInAMonth'),
]