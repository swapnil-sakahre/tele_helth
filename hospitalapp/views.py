from django.shortcuts import render,HttpResponse
from hospitalapp.models import DoctorSpeciality,Hospital,HospitalDoctor,HospitalImages
# Create your views here.
from hospitalapp.models import Hospital
from django.views.generic import *

class HospitalView(ListView):
    model = Hospital
    template_name = 'hospitalapp/hospital_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(HospitalView, self).get_queryset()
       query = self.request.GET.get('search')
       result = Hospital.objects.all()
       # if query:
       #    postresult = Hospital.objects.filter(hospital_name__contains=query)
       #    result = postresult
       # else:
       #     result = Hospital.objects.all()
       return result
class HospitalDetail(DetailView):
    model=Hospital
    template_name = 'hospitalapp/hospital_detail.html'
