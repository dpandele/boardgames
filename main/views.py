from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/home.html",{'message':'Hi, there!'})

def formular(request):
    return render(request, "main/formular.html")

def formular_submit(request):
    return render(request, "main/raspunsformular.html",{'name':request.POST['nume'],'prenume':request.POST['prenume'],
                                                        'trimite':request.POST['trimite']})

from .forms import PersonForm
from .models import Person
def persons(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        return render(request, 'main/persons.html', {'persons': persons})
def deleteperson(request, id):
    if request.method == 'GET':
        Person.objects.all().filter(pk=int(id)).delete()
        persons = Person.objects.all()
    return render(request, 'main/persons.html', {'persons': persons})
def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            person = Person()
            person.nume = cd['nume']
            person.mail = cd['email']
            person.phonenumber = cd['phonenumber']
            person.save()
            form = PersonForm()
        else:
            print("Form is not valid")
    else:
        form = PersonForm()

    return render(request, 'main/contact_form.html', {'form': form})