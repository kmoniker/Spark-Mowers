from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
# Create your models here.

class Customer(models.Model):
    """
    Model representing a lawn mower service Customer
    """

    last_name = models.CharField(max_length=200, help_text="Last name")
    first_name = models.CharField(max_length=200, help_text="First name")
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def fullname(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.fullname()

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


class ServiceInstance(models.Model):
    """
    Model representing a lawn mower Service Instance
    """
    service = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)
    date =  models.DateField(null=True, blank=True)
    cost = models.CharField(max_length=200, help_text="actual charge for service")
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)

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
    service_record = models.ManyToManyField(ServiceInstance, blank=True)

    def __str__(self):
        return "%s's %s" % (self.owner.fullname(), self.brand)

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


class SmallEngineClass(models.Model):
    host = models.CharField(max_length=2000)
    street_address = models.CharField(max_length=2000)
    city = models.CharField(max_length=2000)
    session_1_date = models.DateTimeField()
    session_2_date = models.DateTimeField()
    paid_students = models.IntegerField(default=0)

    def __str__(self):
        self.session_1_date
        return "%s (ID: %s), %s & %s " %(self.city, self.pk, self.format_time(self.session_1_date), self.format_time(self.session_2_date))

    def format_time(self, obj):
        time = obj+timedelta(hours=-6)  #weirdly strftime seems to add 6 hours onto the time...
        time = time.strftime("%a, %b %d at %I %p")
        return time

    def get_name(self):
        return self.__name__

    class Meta:
        verbose_name_plural = "Small Engine Classes"
