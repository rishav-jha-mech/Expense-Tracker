from django.shortcuts import render, redirect
from datetime import datetime
from daApp.models import Expense

def index(request):

    today = datetime.now()
    todays_expenses = Expense.objects.all()
    todays_expenses = todays_expenses.filter(date=today.date())
    monthly_expenses = Expense.objects.filter(date__month=today.month)

    context = {
        'expenses': todays_expenses,
        'monthly_expenses': monthly_expenses,
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