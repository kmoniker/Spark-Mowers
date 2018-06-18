from django.contrib import admin

# Register your models here.
from .models import Customer, ServiceInstance, ServiceType, Employee, LawnMower, ForSale

admin.site.register(Customer)
admin.site.register(ServiceInstance)
admin.site.register(ServiceType)
admin.site.register(Employee)
#admin.site.register(LawnMower)
#admin.site.register(ForSale)

@admin.register(LawnMower)
class LawnMowerAdmin(admin.ModelAdmin):

    list_display = ('brand', 'owner',)
    fieldsets = (
        ('Mower Info', {
            'fields': ('brand','engine_model','chassis_model', 'serial_number', 'spark_plug')
        }),
        ('Owner', {
            'fields': ('owner',)
        }),
        
    )


@admin.register(ForSale)
class ForSaleAdmin(admin.ModelAdmin):
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
            'fields': ('sale_date', 'sale_price', 'sale_customer')
        }),
    )

admin.site.site_header = "Spark Lawn Mower Tune-ups"
