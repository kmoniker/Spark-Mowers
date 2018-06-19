from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from .models import Customer, Employee, LawnMower, ServiceType, ServiceInstance, SaleListing

def index(request):
    return render(
        request,
        'index.html',
        context = {}
    )

def contactus(request):
    return render(
        request,
        'contact-us.html'
    )

def aboutus(request):
    return render(
        request,
        'about-us.html'
    )

from django.views import generic

class ServiceTypeListView(generic.ListView):
    model = ServiceType

class SaleListingListView(LoginRequiredMixin, generic.ListView):
    model = SaleListing
    queryset = SaleListing.objects.filter(sale_date__isnull = True)
    #filter by not sold...

@login_required
def SaleListingDetailView(request,pk):
    try:
        salelisting_id=SaleListing.objects.get(pk=pk)
    except SaleListing.DoesNotExist:
        raise Http404("Listing does not exist")

    return render(
        request,
        'catalog/salelisting_detail.html',
        context={'listing':salelisting_id,}
    )
