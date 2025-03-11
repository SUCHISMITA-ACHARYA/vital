from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from doctors.views import home

urlpatterns = [
    path('admin/', admin.site.urls),  
    path("doctors/", include("doctors.urls")),  # Doctor-related URLs
    path('captcha/', include('captcha.urls')),
    # Add patient-related URLs  # Include patient registration URLs

    path('', home, name='home'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
