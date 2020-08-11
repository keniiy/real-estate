from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import prices_choices, bedroom_choices, state_choices


# Create your views here.
def index(request):
    carousels = Listing.objects.order_by('?').filter(is_published=True)[:3]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    featured = Listing.objects.filter(featured=True).filter(is_published=True).order_by('-list_date')[0:6]
    realtors = Realtor.objects.order_by('hire_date')

    context = {
        'listings': listings,
        'featured': featured,
        'realtors': realtors,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prices_choices': prices_choices,
        'carousels': carousels
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', context)
