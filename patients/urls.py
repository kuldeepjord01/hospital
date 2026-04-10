from django.urls import path
#from . import views
from .views import patient_delete,patient_edit, patient_create
from .views import Patient_list, PatientListCreateApi


urlpatterns=[
    path('', Patient_list.as_view()),
    path('patients/<int:pk>/edit/', patient_edit),
    path('create/', patient_create),
    path('patients/<int:pk>/delete/', patient_delete),
    path('api', PatientListCreateApi.as_view())
]