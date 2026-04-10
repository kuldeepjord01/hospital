from rest_framework import serializers
from .models import Patients   


class PatirentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields ='__all__'