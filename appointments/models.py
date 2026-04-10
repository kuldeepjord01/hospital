from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
class Appointment(models.Model):
    patients = models.ForeignKey('patients.Patients', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return f"{self.patients} - {self.doctor}"