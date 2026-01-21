from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.db.models import Sum

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'total_amount': total_amount
    })

def add_expense(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')
        description = request.POST.get('description')
        location = request.POST.get('location')
        payment_method = request.POST.get('payment_method')
        
        Expense.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=date,
            description=description,
            location=location,
            payment_method=payment_method
        )
        return redirect('expense_list')
    
    return render(request, 'expenses/add_expense.html', {
        'categories': Expense.CATEGORY_CHOICES,
        'payment_methods': Expense.PAYMENT_CHOICES
    })

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expense_list')
