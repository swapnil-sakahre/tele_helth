from doctorapp.models import Doctor
from django import forms

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
