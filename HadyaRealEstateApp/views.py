from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import  price_choices, bedroom_choices, state_choices

# Create your views here.

def index(request):
    listing=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listing,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'HadyaRealEstateApp/index.html',context)
    #return HttpResponse('<h1>Hello World</h1>')

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    #get
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context={
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }

    return render(request,'HadyaRealEstateApp/about.html',context)

def privacy(request):
    return render(request,'HadyaRealEstateApp/privacy.html')

def contactus(request):
    mvp_realtors = Realtor.objects.filter(is_mvp=True)  # Adjust the filter based on your model
    context = {
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'HadyaRealEstateApp/contact.html', context)