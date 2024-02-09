from django.shortcuts import render
from main.models import *


def index_view(request):
    context = {
        'patient': Patient.objects.all()
     }
    return render(request, 'index.html', context)


def search_patient_view(request):
    name = request.GET.get('name')
    context = {
        'search_patients': Patient.objects.filter(name=name)
    }
    return render(request, 'search.html', context)




def patient_single_view(request, pk):
    context = {
        'patient': Patient.objects.get(pk=pk)
    }
    return render(request, 'patient-detail.html', context)




def doctor_details_view(request):
    context = {
        'doctor': Doctor.objects.get(pk=pk)
    }
    return render(request, "doctor-details.html", context)





