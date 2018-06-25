from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
# Create your models here.

class Customer(models.Model):
    """
    Model representing a lawn mower service Customer
    """

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def pretty_phone(self):
        pretty = '%s-%s-%s' % (self.phone_number[:3], self.phone_number[3:6], self.phone_number[6:])
        return pretty

    def last_service(self):
        mowers=self.lawnmower_set.all()
        dates = []
        for m in mowers:
            dates.append(m.last_serviced())
        if len(dates) == 0:
            return None
        else:
            return max(dates)


    def __str__(self):
        return self.name

class ServiceType(models.Model):
    """
    Model representing a lawn mower Service
    """

    service = models.CharField(max_length=200, help_text="name of the service")
    price = models.CharField(max_length=200, help_text="general cost for service")
    description = models.TextField(max_length=2000, help_text="what it includes", blank=True)
    display_on_website = models.BooleanField()

    def __str__(self):
        return self.service

    def get_absolute_url(self):
                return reverse('servicetype-detail', args=[str(self.id)])

class ServiceRecord(models.Model):
    """
    Model representing a lawn mower line item on a service record
    """
    service = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)
    date =  models.DateField(null=True, blank=True)
    cost = models.CharField(max_length=200, help_text="actual charge for service")
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    lawn_mower = models.ForeignKey('LawnMower', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s" % (self.service,self.date)

class LawnMower(models.Model):
    """
    Model representing a LawnMower
    """

    brand = models.CharField(max_length=200)
    engine_model = models.CharField(max_length=200, help_text="model number of the engine", blank=True)
    chassis_model = models.CharField(max_length=200, help_text="model number of the chassis", blank=True)
    spark_plug = models.CharField(max_length=200)
    owner = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    notes = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return "%s's %s" % (self.owner.name, self.brand)

    def last_service(self):
        service = self.servicerecord_set.all().latest('date')
        return service.service

    def last_serviced(self):
        service = self.servicerecord_set.all().latest('date')
        return service.date

class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SaleListing(models.Model):
    picture = models.ImageField(upload_to="gallery")
    lawn_mower = models.ForeignKey('LawnMower', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000)
    list_price = models.CharField(max_length=20)
    list_date = models.DateField()
    sale_price = models.CharField(max_length=20, null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)

    def __str__(self):
        #return "%s %s" % (self.lawn_mower.brand, self.list_price)
        return "%s" % (self.pk)

    def get_absolute_url(self):
                return reverse('salelisting-detail', args=[str(self.id)])
