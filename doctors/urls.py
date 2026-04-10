from django.urls import path
from . import views
from .views import doctor_list, doctor_create, doctor_delete
from .views import DoctorListCreateApi


urlpatterns=[
    path('', doctor_list, name='doctor_list'),
    path('create/', doctor_create, name='doctor_create'),
    path('<int:id>/edit/', views.doctor_edit, name='doctor_edit'),
    path('<int:id>/delete/', views.doctor_delete, name='doctor_delete'),
    path('api', DoctorListCreateApi.as_view())
]