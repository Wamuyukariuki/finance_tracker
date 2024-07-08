from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.template import loader

from .forms import TransactionForm
from .models import Transaction


# List all transactions (paginated for mobile view)
# @login_required(optional)  # Comment out if not using user authentication
def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')  # Order by recent first
    paginator = Paginator(transactions, 10)  # Paginate for 10 transactions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'transactions': page_obj}
    template = loader.get_template('tracker/transaction_list.html')
    return render(request, 'tracker/transaction_list.html', context)


# Create a new transaction
# @login_required(optional)  # Comment out if not using user authentication
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')  # Redirect to list view after creation
    else:
        form = TransactionForm()
    context = {'form': form}
    return render(request, 'tracker/transaction_create.html', context)


# Update an existing transaction (optional)
# @login_required(optional)  # Comment out if not using user authentication
def transaction_update(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')  # Redirect to list view after update
    else:
        form = TransactionForm(instance=transaction)
    context = {'form': form}
    return render(request, 'tracker/transaction_update.html', context)


# Delete a transaction (optional)
# @login_required(optional)  # Comment out if not using user authentication
def transaction_delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')  # Redirect to list view after delete
    context = {'transaction': transaction}
    return render(request, 'tracker/transaction_delete.html', context)
