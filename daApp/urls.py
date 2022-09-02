from django.urls import path
from daApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detailed-daywise', views.detailedDaywise, name='detailedDaywise'),
    path('daily-report', views.dailyReport, name='dailyReport'),
    path('all-detail', views.allDetail, name='allDetail'),
    path('monthly-report', views.monthlyReport, name='monthlyReport'),
    path('expense-on-a-date/<slug:slug>', views.expenseOnADate, name='expenseOnADate'),
    path('expense-on-a-month', views.expenseOnAMonth, name='expenseOnAMonth'),
    path('total-expense-in-a-day/<slug:slug>', views.totalExpenseInADay, name='totalExpenseInADay'),
    path('total-expense-in-a-month', views.totalExpenseInAMonth, name='totalExpenseInAMonth'),
]