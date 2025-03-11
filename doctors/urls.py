from django.urls import path
from . import views
from .views import (
    register_doctor,profile, home,  vacc_form, vacc_result
   
)
from django.views.generic import TemplateView

app_name = "doctors"  # Keeps URL namespaced

urlpatterns = [
    # Home Page (if needed)
    path("", home, name="home"),
    
    
    # Doctor Routes
    path("register/", register_doctor, name="register"),
    path('profile/<int:doctor_id>/',profile, name='profile'),
    path('search/', views.search_doctors, name='search_doctors'),
    path("form/", vacc_form, name="vacc_form"),
    path("result/", vacc_result, name="vacc_result"),
]
