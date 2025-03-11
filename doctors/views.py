from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import DoctorRegistrationForm
from .models import Doctor

def home(request):
    """Renders the home page."""
    return render(request, 'home.html')

def doctor_dashboard(request):
    """Renders the doctor's dashboard page."""
    return render(request, 'doctors/doctor_dashboard.html')

def register_doctor(request):
    if request.method == "POST":
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save()  # Save form and get doctor object
            messages.success(request, "Doctor registered successfully!")  # Success message
            request.session['success_message'] = "Doctor registered successfully!"  # Store message in session
            return redirect("doctors:profile", doctor_id=doctor.id)  # Redirect to profile
        else:
            messages.error(request, "Please correct the errors below.")  # Show error message
    else:
        form = DoctorRegistrationForm()

    return render(request, "doctors/register.html", {"form": form})

def profile(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    
    # Retrieve success message from session
    success_message = request.session.pop('success_message', None)

    return render(request, "doctors/profile.html", {"doctor": doctor, "success_message": success_message})

def search_doctors(request):
    # Fetch distinct specialties and cities from the database
    specialties = Doctor.objects.values_list('specialist', flat=True).distinct()
    cities = Doctor.objects.values_list('Clinic_City', flat=True).distinct()

    # Get search inputs from the request
    specialty_query = request.GET.get('specialist', '')  # Get specialty from form
    city_query = request.GET.get('city', '')  # Get city from form

    # Filtering doctors based on user input
    doctors = Doctor.objects.all()
    if specialty_query:
        doctors = doctors.filter(specialist__icontains=specialty_query)
    if city_query:
        doctors = doctors.filter(Clinic_City__icontains=city_query)

    return render(request, 'search.html', {
        'specialties': specialties,
        'cities': cities,
        'query': specialty_query,
        'city_query': city_query,
        'doctors': doctors
    })

def get_vaccinations(age, gender):
    age = int(age)  # Convert age to integer for comparison
    vaccinations = []

    # Vaccination data categorized by age groups
VACCINATION_SCHEDULE = [
        # Infants & Children
        {"age": 0, "name": "BCG, Hepatitis B (1st dose)", "notes": "Protects against tuberculosis and hepatitis B"},
        {"age": 1, "name": "MMR (1st dose), Varicella (1st dose), Hepatitis A (1st dose)", 
     "notes": "Protects against measles, mumps, rubella, chickenpox, and hepatitis A"},
    
        {"age": 1.5, "name": "DTP Booster (1st), Hib Booster, IPV Booster, Influenza (annual)", 
     "notes": "Boosts immunity against diphtheria, tetanus, pertussis, polio, and flu"},
    
        {"age": 2, "name": "Typhoid (1st dose), Influenza (annual)", 
     "notes": "Prevents typhoid and flu"},
    
        {"age": 3, "name": "MMR (2nd dose), Varicella (2nd dose), Hepatitis A (2nd dose), Influenza (annual)", 
     "notes": "Provides long-term immunity against MMR, chickenpox, hepatitis A, and flu"},
    
        {"age": 4, "name": "DTP Booster (2nd), IPV Booster, PCV Booster, Influenza (annual)", 
     "notes": "Further strengthens immunity against diphtheria, tetanus, pertussis, polio, pneumonia, and flu"},
    
        {"age": 5, "name": "Typhoid Booster, Meningococcal Vaccine, Influenza (annual)", 
     "notes": "Continued protection against typhoid, meningitis, and flu"},
        {"age": 6, "name": "DPT (1st dose), Rotavirus, Hib, PCV, IPV, Hep B (2nd dose)", "notes": "Prevents diphtheria, whooping cough, pneumonia, and hepatitis B"},
        {"age": 10, "name": "DPT (2nd dose), Hib (2nd dose), PCV (2nd dose), IPV (2nd dose)", "notes": "Follow-up for stronger immunity"},
        {"age": 14, "name": "DPT (3rd dose), Hib (3rd dose), PCV (3rd dose), IPV (3rd dose), Rotavirus", "notes": "Last primary series doses"},
        {"age": 6, "name": "Influenza (annual)", "notes": "Protects against flu"},
        {"age": 9, "name": "Measles, Mumps, Rubella (MMR - 1st dose), Yellow Fever", "notes": "Prevents serious viral infections"},
        {"age": 12, "name": "Hepatitis A (1st dose), Typhoid", "notes": "Prevents foodborne diseases"},
        {"age": 15, "name": "MMR (2nd dose), Varicella (Chickenpox), PCV Booster", "notes": "Boosts long-term immunity"},
        {"age": 18, "name": "DPT Booster, IPV Booster, Hib Booster", "notes": "Strengthens childhood immunization"},
        {"age": 24, "name": "Influenza (annually), Typhoid Booster", "notes": "Continued immunity"},

        # Adolescents
        {"age": 10, "name": "HPV Vaccine (Females only)", "notes": "Prevents cervical cancer", "gender": "female"},
        {"age": 12, "name": "Tdap Booster", "notes": "Protects against diphtheria, tetanus, pertussis"},
        {"age": 16, "name": "Meningococcal (MCV), Hepatitis A (2nd dose)", "notes": "Prevents bacterial meningitis"},

        # Adults
        {"age": 18, "name": "HPV Vaccine (Catch-up for Males & Females)", "notes": "Prevents certain cancers"},
        {"age": 18, "name": "Annual Influenza, Hepatitis B (if not taken earlier)", "notes": "Protection against flu and liver disease"},
        {"age": 40, "name": "Shingles (Herpes Zoster)", "notes": "Prevents painful rash"},
        {"age": 50, "name": "Pneumococcal Vaccine", "notes": "Prevents pneumonia"},
        {"age": 60, "name": "COVID-19 Booster, Tdap Booster", "notes": "Immunity maintenance"},
    ]

   


# View for vaccination form page
def vacc_form(request):
    return render(request, "vacc.html")


# View for vaccination results page


def vacc_result(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))

        # Missed vaccinations (ages less than the entered age)
        missed_vaccinations = [v for v in VACCINATION_SCHEDULE if v["age"] < age]

        # Upcoming vaccinations (ages greater than or equal to the entered age)
        upcoming_vaccinations = sorted(
            [v for v in VACCINATION_SCHEDULE if v["age"] >= age], 
            key=lambda x: x["age"]
        )

        return render(request, "vacre.html", {
            "missed_vaccinations": missed_vaccinations,
            "upcoming_vaccinations": upcoming_vaccinations
        })
    else:
        return render(request, "vacc.html")

