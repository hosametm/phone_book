from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact, Phone


# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        phones = request.POST.getlist('phones[]')  # Get list of phone numbers
        contact = Contact.objects.create(name=name)
        for phone in phones:
            Phone.objects.create(contact=contact, phone=phone)

        return redirect("/contacts/")
    else:
        return render(request, 'contacts/create.html')


def view(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    phones = Phone.objects.filter(contact=contact)
    context = {'contact': contact, 'phones': phones}
    return render(request, 'contacts/view.html', context)
