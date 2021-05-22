from django.shortcuts import render
from .models import aboutus
from .models import slider_us
from .models import our_client


# Create your views here.
def home(request):
    aboutdata = aboutus.objects.all()[0]
    sliderdata = slider_us.objects.all()
    clintsdata = our_client.objects.all()
    context={
        'about_des':aboutdata,
        'my_slider':sliderdata,
        'clients_team':clintsdata
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

