from django.urls import path
from .views import dashboard, dashboard_hms_ai, user_logout, Appointment, Patients, Doctor

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logout/', user_logout, name='dashboard_logout'),
    path('ai/', dashboard_hms_ai, name='dashboard_hms_ai'),
] 
 