# Generated by Django 5.1.6 on 2025-03-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctor_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='clinic_number',
            new_name='clinic_contact_number',
        ),
    ]
