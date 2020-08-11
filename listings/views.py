from django.shortcuts import render, get_object_or_404

from .choices import state_choices, bedroom_choices, prices_choices
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.


def index(request):
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
        'mvp_realtor': mvp_realtor,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Filter by exact state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Filter by max bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Filter by max price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prices_choices': prices_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
