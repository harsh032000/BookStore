from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm
from .filters import BookFilter
# Create your views here.

def index(request):
    total=Book.objects.count()
    return render(request, 'index.html',{'total' : total})

def products(request):
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    return render(request, 'products.html', {'books': books, 'myFilter' : myFilter})

def addbook(request):
    total=Book.objects.count()
    form=BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    return render(request, 'addbook.html',{'total': total, 'form':form})