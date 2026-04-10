from django.urls import path

from dashboard import views
from .views import appointment_create, appointment_list, appointment_edit

urlpatterns = [
    path('', appointment_list, name='appointment_list'),
    path('<int:id>/edit/', appointment_edit, name='appointment_edit'),
    path('create/',appointment_create, name='appointment_create'),   

]