from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime, timedelta
from daApp.models import Expense, Balance
from daApp.utils import date_range_list

def index(request):

    today = datetime.now()
    total_expenses = Expense.objects.all()
    todays_expenses = total_expenses.filter(date=today.date())
    monthly_expenses = Expense.objects.filter(date__month=today.month)

    context = {
        'date': today.date(),
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

def detailedDaywise(request):
    date = request.GET.get('date')
    if date is None:
        date = datetime.now().date()
    expenses = Expense.objects.filter(date=date)
    context = {
        'expenses': expenses,
        'date' : date,
    }
    
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'DELETE_EXPENSE':
            expense_id = request.POST.get('id')
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return redirect(f'/detailed-daywise?date={date}')

        if action == 'EDIT_EXPENSE':
            expense_id = request.POST.get('id')
            expense = Expense.objects.get(id=expense_id)
            expense.date=request.POST.get('date')
            expense.amount=request.POST['amount']
            expense.person=request.POST['person']
            expense.category=request.POST['category']
            expense.description=request.POST['desc']
            expense.save()
            return redirect(f'/detailed-daywise?date={date}')

        if action == 'ADD_EXPENSE':
            expense = Expense(
                date=request.POST['date'],
                amount=request.POST['amount'],
                person=request.POST['person'],
                category=request.POST['category'],
                description=request.POST['desc'],
            )
            expense.save()
            return redirect(f'/detailed-daywise?date={date}')

    return render(request, 'detailedDaywise.html', context)

def allDetail(request):
    sort = request.GET.get('sort')
    if sort is None:
        sort = '-date'
    expenses = Expense.objects.all().order_by(sort)
    context = {
        'expenses': expenses,
    }
    return render(request, 'allDetail.html', context)

def dailyReport(request):

    today7 = datetime.now() - timedelta(days=7)
    today15 = datetime.now() - timedelta(days=15)
    today30 = datetime.now() - timedelta(days=30)
    date_list7 = date_range_list(today7, today7 + timedelta(days=7))
    date_list15 = date_range_list(today15, today15 + timedelta(days=15))
    date_list30 = date_range_list(today30, today30 + timedelta(days=30))
    datas7 = []
    datas15 = []
    datas30 = []
    for date in date_list7:
        daDate = date.strftime('%Y-%m-%d')
        expenses = Expense.objects.filter(date=daDate)
        total = sum([expense.amount for expense in expenses])
        datas7.append({'date': date, 'total': total})
    
    for date in date_list15:
        daDate = date.strftime('%Y-%m-%d')
        expenses = Expense.objects.filter(date=daDate)
        total = sum([expense.amount for expense in expenses])
        datas15.append({'date': date, 'total': total})
    
    for date in date_list30:
        daDate = date.strftime('%Y-%m-%d')
        expenses = Expense.objects.filter(date=daDate)
        total = sum([expense.amount for expense in expenses])
        datas30.append({'date': date, 'total': total})
    context = {
        'datas' : datas7,
        'datas15' : datas15,
        'datas30' : datas30,
    }
    return render(request, 'dailyReport.html', context)

def monthlyReport(request):
    today = datetime.now()
    datas = []
    for month in range(1,13):
        expenses = Expense.objects.filter(date__month=month,date__year=today.year)
        total = sum([expense.amount for expense in expenses])
        datas.append(total)

    context = {
        'datas' : datas,
    }
    return render(request, 'monthlyReport.html', context)

def expenseOnADate(request,slug):
    expenses = Expense.objects.filter(date=slug).values()
    return JsonResponse({'data': list(expenses)}, safe=False)

def expenseOnAMonth(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None:
        return JsonResponse({'data': []}, safe=False)
    expenses = Expense.objects.filter(date__month=month,date__year=year).values()
    return JsonResponse({'data': list(expenses)}, safe=False)

def totalExpenseInADay(request,slug):
    expenses = Expense.objects.filter(date=slug)
    sum = 0
    for expense in expenses:
        sum += expense.amount
    return JsonResponse({'data': sum}, safe=False)

def totalExpenseInAMonth(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    if year is None or month is None:
        return JsonResponse({'data': 'Wrong Improper Month or Year params'}, safe=False)
    total = sum(iterable=expenses.values_list('amount', flat=True))
    return JsonResponse({'data': total}, safe=False)