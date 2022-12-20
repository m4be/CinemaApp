from django.shortcuts import render,redirect
# Create your views here.
from .forms import PersonForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def adam(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-adam.html',data)

def adams(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-adams.html',data)

def amsterdam(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-amsterdam.html',data)

def avatar(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-avatar.html',data)

def elki(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-elki.html',data)

def fall(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-fall.html',data)

def fallout(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-fallout.html',data)

def heart(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-heart.html',data)

def panther(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-panther.html',data)

def potter(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-potter.html',data)

def shel(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-shel.html',data)

def troll(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket-troll.html',data)

def buyTicketTESTDELETEE(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    form = PersonForm()
    data = {
        'form':form,
    }
    return render(request, 'main/buy-ticket.html',data)



