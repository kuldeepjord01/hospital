from django.shortcuts import get_object_or_404, render, redirect

from patients.models import Patients
from .models import Doctor
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def doctor_list(request):
    doctors= Doctor.objects.all()
    return render(request, 'index.html',{'doctors':doctors})

@login_required
def doctor_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id) 
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.phone = request.POST.get('phone')
        doctor.specialization = request.POST.get('specialization')
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doc_edit.html',{'doctor':doctor})

@login_required
def doctor_create(request):
    if request.method == 'POST':
          doctor = Doctor()
          doctor.name = request.POST.get('name')
          doctor.phone = request.POST.get('phone')
          doctor.specialization = request.POST.get('specialization')

          Doctor.objects.create(name=doctor.name, phone=doctor.phone, specialization=doctor.specialization) 
        
          return redirect('doctor_list')
    return render(request, 'doc_create.html')

@login_required
def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    doctor.delete()
    return redirect('/doctors/')
    


from rest_framework.generics import ListCreateAPIView
from .serializers import DoctorSerializer 

class DoctorListCreateApi(ListCreateAPIView):
     queryset = Doctor.objects.all()
     serializer_class = DoctorSerializer
     