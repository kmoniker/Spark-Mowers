from django.contrib import admin
from django.forms import CheckboxSelectMultiple
# Register your models here.
from .models import *

# admin.site.register(Customer)
admin.site.register(ServiceRecord)
admin.site.register(ServiceType)
admin.site.register(Employee)
#admin.site.register(LawnMower)
#admin.site.register(SaleListing)
# admin.site.register(SmallEngineClass)

class ServiceRecordInline(admin.TabularInline):
    model = ServiceRecord

class LawnMowerInline(admin.TabularInline):
    model = LawnMower

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_number','email', 'last_service')
    fields = ('name','address','phone_number','email','notes')
    inlines = [LawnMowerInline,]

@admin.register(LawnMower)
class LawnMowerAdmin(admin.ModelAdmin):

    list_display = ('brand', 'owner','last_serviced')
    inlines = [ServiceRecordInline,]
    fieldsets = (
        ('Mower Info', {
            'fields': ('brand','engine_model','chassis_model', 'spark_plug', 'notes')
        }),
        ('Owner', {
            'fields': ('owner',)
        }),
    )


@admin.register(SaleListing)
class SaleListingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'list_date', 'list_price', 'sale_date', 'sale_price')
    list_filter = ('sale_date',)
    fieldsets = (
        (None, {
            'fields': ('lawn_mower','picture','description')
        }),
        ('Listing', {
            'fields': ('list_date', 'list_price')
        }),
        ('Sale', {
            'fields': ('sale_date', 'sale_price')
        }),
    )
