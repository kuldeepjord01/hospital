
from django.shortcuts import render
from .models import Marketing

def home(request):
    home= Marketing.objects.all()
    return render(request, 'marketing_home.html', {"home":home})   