from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm()
    return render(request, 'form.html', {'form': form})

def contact(request):
    return render(request, 'contact.html') 

