from django.shortcuts import render
from .models import *
# Create your views here.

def services(request):
    service_b=Services_a.objects.filter(status=True)
    service=Services.objects.filter(status=True)
    context={
        'service':service,
        'services':service_b
    }
    return render(request,'services/services.html',context=context)