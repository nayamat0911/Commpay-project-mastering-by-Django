from django.shortcuts import render
from .models import contact_us

# Create your views here.

def contact(request):
    if request.method=='POST':
        name_a = request.POST.get('contact_name')
        email_a = request.POST.get('contact_email')
        subject_a = request.POST.get('contact_subject')
        massege_a = request.POST.get('contact_message')

        contact_data=contact_us(name=name_a, email=email_a, subject=subject_a, massege=massege_a)
        contact_data.save()

    return render(request,'contact.html')