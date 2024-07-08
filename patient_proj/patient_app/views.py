from django.shortcuts import render, HttpResponse, redirect
from .models import Patient
# Create your views here.

#apis
from .serializers import PatientSerializer
from rest_framework import viewsets

class PatientModelViewSet(viewsets.ModelViewSet):
     queryset = Patient.objects.all()
     serializer_class = PatientSerializer

#all patients
def index(request):
    patient = Patient.objects.all()
    context = {
        'patient' : patient
    }
    return render(request, 'home.html', context)

#add patient
def add_patient(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']

        new_patient = Patient(first_name=first_name, last_name=last_name,
                              email=email, phone=phone, dob=dob)
        new_patient.save()

        return redirect('home')


    return render(request, 'home.html')

#update patient
def edit_patient(request):
    patient = Patient.objects.all()
    context = {
        'patient' : patient
    }
   
    return redirect('home')

def update_patient(request, pk):
        if request.method=="POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            dob = request.POST['dob']

            update_patient = Patient(
                 id=pk,
                 first_name=first_name, last_name=last_name,
                email=email, phone=phone, dob=dob)
            update_patient.save()

            return redirect('home')
        

def delete_patient(request, pk):
     _patient = Patient.objects.get(id=pk)
     _patient.delete()
     return redirect('home')