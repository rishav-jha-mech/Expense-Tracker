from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from daApp.models import Expense

def index(request):

    today = datetime.now()
    total_expenses = Expense.objects.all()
    todays_expenses = total_expenses.filter(date=today.date())
    monthly_expenses = Expense.objects.filter(date__month=today.month)

    context = {
        'expenses': todays_expenses,
        'monthly_expenses': monthly_expenses,
        'total_expenses': total_expenses,
    }

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'DELETE_EXPENSE':
            expense_id = request.POST.get('id')
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return redirect('index')

        if action == 'EDIT_EXPENSE':
            expense_id = request.POST.get('id')
            expense = Expense.objects.get(id=expense_id)
            expense.date=request.POST.get('date')
            expense.amount=request.POST['amount']
            expense.person=request.POST['person']
            expense.category=request.POST['category']
            expense.description=request.POST['desc']
            expense.save()
            return redirect('index')

        if action == 'ADD_EXPENSE':
            expense = Expense(
                date=request.POST['date'],
                amount=request.POST['amount'],
                person=request.POST['person'],
                category=request.POST['category'],
                description=request.POST['desc'],
            )
            expense.save()
            return redirect('index')

    return render(request, 'index.html', context)

def detailedToday(request):
    today = datetime.now()
    expenses = Expense.objects.filter(date=today.date())
    context = {
        'expenses': expenses,
    }
    return render(request, 'detailedToday.html', context)

def expenseOnADate(request):
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None or day is None:
        return JsonResponse({'data': []}, safe=False)
    expenses = Expense.objects.filter(date__month=month, date__day=day, date__year=year).values()
    return JsonResponse({'data': list(expenses)}, safe=False)

def expenseOnAMonth(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None:
        return JsonResponse({'data': []}, safe=False)
    expenses = Expense.objects.filter(date__month=month,date__year=year).values()
    return JsonResponse({'data': list(expenses)}, safe=False)

def totalExpenseInADay(request):
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None or day is None:
        return JsonResponse({'data': 'Wrong Improper Month, Year, or Day params'}, safe=False)
    expenses = Expense.objects.filter(date__month=month, date__day=day, date__year=year)
    total = sum(iterable=expenses.values_list('amount', flat=True))
    return JsonResponse({'data': total}, safe=False)

def totalExpenseInAMonth(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None:
        return JsonResponse({'data': 'Wrong Improper Month or Year params'}, safe=False)
    total = sum(iterable=expenses.values_list('amount', flat=True))
    return JsonResponse({'data': total}, safe=False)