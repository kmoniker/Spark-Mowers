from django.db import models
from django.urls import reverse
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
    engine_model = models.CharField(max_length=200, help_text="model number of the engine")
    chassis_model = models.CharField(max_length=200, help_text="model number of the chassis")
    serial_number = models.CharField(max_length=200, help_text="serial number")
    spark_plug = models.CharField(max_length=200)
    owner = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    service_record = models.ManyToManyField(ServiceInstance, blank=True)

    def __str__(self):
        return "%s's %s" % (self.owner.fullname(), self.brand)

class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ForSale(models.Model):
    brand = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="gallery")
    list_price = models.CharField(max_length=20)
    list_date = models.DateField()
    sale_price = models.CharField(max_length=20, null=True, blank=True)
    sale_date = models.DateField(null=True, blank=True)
    sale_customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.brand, self.list_price)

    def get_absolute_url(self):
                return reverse('forsale-detail', args=[str(self.id)])
    class Meta:
        verbose_name_plural= 'For Sale'
