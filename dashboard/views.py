from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from patients.models import Patients
from doctors.models import Doctor
from appointments.models import Appointment
import google.generativeai as genai
from django.conf import settings
from markdown_it import MarkdownIt

@login_required
def dashboard(request):
    context = {
        'patients_count': Patients.objects.count(),
        'doctors_count': Doctor.objects.count(),
        'appointments_count': Appointment.objects.count(),
    }
    return render(request, "dashboard_home.html")

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_hms_ai(request):
    answer = None
    error_message = None
    
    if request.method == 'POST':
        try:
            user_query = request.POST.get('query')
            
            if not user_query or user_query.strip() == '':
                error_message = "Please enter a question."
            else:
                # Configure the API key
                genai.configure(api_key=settings.GEMINI_API_KEY)
                
                # Get database data
                doctors = Doctor.objects.all()
                appointments = Appointment.objects.all()
                patients = Patients.objects.all()

                final_query = f'''
            You are the AI chatbot inside a website called medhaHMS
            You responsibility is to answer questions about
            medhaHMS data. Anything part from this, you are not allowed to
            answer. Below is the doctor data you need to know. 
            {doctors} and below are patients {patients}
            and below are appointments {appointments}

            answer below:
            {user_query}
            '''
                
                # Generate response using Gemini API
                model = genai.GenerativeModel("gemini-3-flash-preview")
                response = model.generate_content(final_query)
                
                # Convert markdown to HTML
                md = MarkdownIt()
                answer = md.render(response.text)
                
        except Exception as e:
            error_message = f"Error connecting to AI service: {str(e)}"
            print(f"Gemini API Error: {str(e)}")

    return render(request, 'dashboard_hms_ai.html', {'answer': answer, 'error_message': error_message})