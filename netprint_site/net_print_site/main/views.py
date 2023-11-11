from django.shortcuts import render, redirect
from main.forms import OffersForm
from main.models import Offers

import telebot
bot = telebot.TeleBot('6434629302:AAEpVlT29pZfY3kryTMnYOnk2SYjFFhiFw0')
# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = OffersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
        else:
            error = f"{form}"
            
    form = OffersForm()
    data = {
        'form' : form,
        'error' : error
    }
    print(Offers.objects.last())
    return render(request, "main/index.html", data)

def cont(response):
   
    return render(response, "main/contacts.html" )

def show_success(response):
    data = {}
    return render(response, "main/supa.html")
