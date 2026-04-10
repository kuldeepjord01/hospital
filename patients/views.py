from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django import views
import patients
from .models import Patients
from django.contrib.auth.decorators import login_required
from .forms import PatientForm



# FBV

# @login_required
# def patient_list(request):
#     patients= Patients.objects.all()
#     return render(request, 'list.html', {"patients":patients})

#CBV
class Patient_list(views.View):
     def get(self, request):
          patients= Patients.objects.all()
          return render(request, 'list.html', {"patients":patients})




@login_required
def patient_edit(request, pk):
    patients = get_object_or_404(Patients, pk=pk) 
    if request.method =='POST':
            patients.name = request.POST.get('name')
            patients.phone = request.POST.get('phone')
            patients.email = request.POST.get('email')
            patients.age = request.POST.get('age')
            patients.address =request.POST.get('address')
            patients.save()
            return redirect('/patients')
    return render(request, 'patient_edit.html',{'patients':patients})

    
@login_required
def patient_create(request):
    if request.method == 'POST':
        patients.name = request.POST.get('name')
        patients.phone = request.POST.get('phone')
        patients.email = request.POST.get('email')
        patients.age = request.POST.get('age')
        patients.address =request.POST.get('address')

        Patients.objects.create(
            name=patients.name,
            phone=patients.phone,
            email=patients.email,
            age=patients.age,
            address=patients.address
        )
        return redirect('/patients')
    return render(request, "patient_create.html")


@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    else:
        form = PatientForm()
    return render(request, "patient_create.html", {'form': form})




@login_required
def patient_delete(request, pk):
    patients = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        patients.delete()
    
    return redirect('/patients')
  
     
from rest_framework.generics import ListCreateAPIView
from .serializers import PatirentSerializer

class PatientListCreateApi(ListCreateAPIView):
     queryset = Patients.objects.all()
     serializer_class = PatirentSerializer