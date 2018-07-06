from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.views import generic

from datetime import datetime

from .models import *

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


class ServiceTypeListView(generic.ListView):
    model = ServiceType
    queryset = ServiceType.objects.filter(display_on_website = True)

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

@login_required
def crm(request):
    return render(
        request,
        'crm.html'
    )

class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    queryset = Customer.objects.order_by('name')

class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer

class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = '__all__'

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = '__all__'

class LawnMowerListView(LoginRequiredMixin, generic.ListView):
    model = LawnMower

class LawnMowerDetailView(LoginRequiredMixin, generic.DetailView):
    model = LawnMower

class LawnMowerCreate(LoginRequiredMixin, CreateView):
    model = LawnMower
    fields = '__all__'
    def get_initial(self):
        return {'owner':self.kwargs['custfk']}

class LawnMowerUpdate(LoginRequiredMixin, UpdateView):
    model = LawnMower
    fields = '__all__'

class ServiceRecordCreate(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    fields = '__all__'
    def get_initial(self):
        return {'lawn_mower':self.kwargs['mowerfk']}

class ServiceRecordUpdate(LoginRequiredMixin, UpdateView):
    model = ServiceRecord
    fields = '__all__'

@login_required
def hours(request):
    return render(
        request,
        'hours.html'
    )
