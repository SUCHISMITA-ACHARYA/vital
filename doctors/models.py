from django.db import models

class Doctor(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    PROFILE_SUGGESTION_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    degree = models.CharField(max_length=200)
    specialist = models.CharField(max_length=200, blank=True, null=True)
    aadhar = models.CharField(max_length=20, unique=True)  # Aadhar/Authentication
    certificate = models.FileField(upload_to='certificates/', blank=True, null=True) 
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    Clinic_Name = models.CharField(max_length=255, blank=True, null=True)
    Clinic_address = models.TextField(blank=True, null=True)
    Clinic_City = models.CharField(max_length=15, blank=True, null=True)
    Clinic_Contact_Number = models.CharField(max_length=15, blank=True, null=True)
    profile_suggestion = models.CharField(max_length=3, choices=PROFILE_SUGGESTION_CHOICES)
    contact_through_app = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialist}"
    

