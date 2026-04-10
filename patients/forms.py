from django import forms
from .models import Patients


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['name', 'phone', 'email', 'age', 'address']