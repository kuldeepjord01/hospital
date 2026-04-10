from django.shortcuts import render, get_object_or_404, redirect

import appointments
from doctors.models import Doctor
from patients.models import Patients
from .models import Appointment

# Create your views here.

def appointment_list(request):
    appointments = Appointment.objects.select_related('doctor', 'patients').all()
    return render(request, 'data_list.html', {'appointments': appointments})


def appointment_create(request):
    appointment = Appointment()
    if request.method == 'POST':
        appointment.patients_id = request.POST.get('patients')
        appointment.doctor_id = request.POST.get('doctor')
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_status = request.POST.get('appointment_status')

        Appointment.objects.create(
            patients_id=appointment.patients_id,
            doctor_id=appointment.doctor_id,
            appointment_time=appointment.appointment_time,
            appointment_status=appointment.appointment_status
        )
        return redirect('appointment_list')
    patients = Patients.objects.all()
    doctors = Doctor.objects.all()
    
    return render(request, 'appointment_create.html', {'patients': patients, 'doctors': doctors})


def appointment_edit(request, id):
    appointment= Appointment.objects.get(id=id)
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        appointment.appointment_status = request.POST.get('status')
        
        appointment.save()
        return redirect('appointment_list')
    
    return render(request, 'appointment_edit.html',{'appointment':appointment})
