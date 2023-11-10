from django.shortcuts import render, redirect
from main.forms import OffersForm

# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = OffersForm(request.POST, request.FILES)
        print (form.is_valid())
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
    return render(request, "main/index.html", data)

def cont(response):
   
    return render(response, "main/contacts.html" )

def show_success(response):
    data = {}
    return render(response, "main/supa.html")
