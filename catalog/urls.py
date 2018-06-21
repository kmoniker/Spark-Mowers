from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.ServiceTypeListView.as_view(), name='services'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('about-us/', views.aboutus, name='about-us'),
    path('for-sale/', views.SaleListingListView.as_view(), name='for-sale'),
    path('for-sale/<int:pk>', views.SaleListingDetailView, name='salelisting-detail'),
    # path('classes/', views.SmallEngineClassListView.as_view(), name='classes'),
    path('classes/', views.SmallEngineClassListView, name='classes'),
    path('crm/', views.crm, name='crm'),
    path('crm/customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('crm/lawn-mowers/', views.LawnMowerListView.as_view(), name='lawn_mower-list'),
]
