from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from .models import Customer, Employee, LawnMower, ServiceType, ServiceInstance, ForSale

def index(request):

    num_customers = Customer.objects.all().count()

    return render(
        request,
        'index.html',
        context = {'num_customers':num_customers}
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

class ForSaleListView(LoginRequiredMixin, generic.ListView):
    model = ForSale
    queryset = ForSale.objects.filter(sale_date__isnull = True)
    #filter by not sold...

@login_required
def ForSaleDetailView(request,pk):
    try:
        forsale_id=ForSale.objects.get(pk=pk)
    except ForSale.DoesNotExist:
        raise Http404("Mower does not exist")

    return render(
        request,
        'catalog/forsale_detail.html',
        context={'mower':forsale_id,}
    )
