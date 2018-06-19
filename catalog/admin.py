from django.contrib import admin

# Register your models here.
from .models import Customer, ServiceInstance, ServiceType, Employee, LawnMower, SaleListing, SmallEngineClass

admin.site.register(Customer)
admin.site.register(ServiceInstance)
admin.site.register(ServiceType)
admin.site.register(Employee)
#admin.site.register(LawnMower)
#admin.site.register(SaleListing)
# admin.site.register(SmallEngineClass)

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

@admin.register(SmallEngineClass)
class SmallEngineClassAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'session_1_date', 'session_2_date')
admin.site.site_header = "Spark Lawn Mower Tune-ups"
