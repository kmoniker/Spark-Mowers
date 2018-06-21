from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from .forms import EmailSignupForm
from .models import Customer, Employee, LawnMower, ServiceType, ServiceRecord, SaleListing, SmallEngineClass

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
    queryset = ServiceType.objects.filter(display_on_website = True)

# class SmallEngineClassListView(generic.ListView):
#     model = SmallEngineClass
#     queryset = SmallEngineClass.objects.filter(session_1_date__gte = datetime.today())

class SaleListingListView(LoginRequiredMixin, generic.ListView):
    model = SaleListing
    queryset = SaleListing.objects.filter(sale_date__isnull = True)
    #filter by not sold...

def SmallEngineClassListView(request):
    smallengineclass_list = SmallEngineClass.objects.filter(session_1_date__gte = datetime.today())
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = EmailSignupForm(request.POST)
    # If this is a GET (or any other method) create the default form.
    else:
        form = EmailSignupForm()

    return render(
        request,
        'catalog/smallengineclass_list.html',
        context={'smallengineclass_list':smallengineclass_list,'form':form,}
    )

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

@login_required
def crm(request):
    return render(
        request,
        'crm.html'
    )

class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer

class LawnMowerListView(LoginRequiredMixin, generic.ListView):
    model = LawnMower
