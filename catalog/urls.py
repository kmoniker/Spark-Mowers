from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.ServiceTypeListView.as_view(), name='services'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('about-us/', views.aboutus, name='about-us'),
    path('for-sale/', views.SaleListingListView.as_view(), name='for-sale'),
    path('for-sale/<int:pk>', views.SaleListingDetailView, name='salelisting-detail'),
    path('crm/', views.CustomerListView.as_view(), name='crm'),
    path('crm/customer/<int:pk>', views.CustomerDetailView.as_view(), name='view-customer'),
    path('crm/customer/edit/<int:pk>', views.CustomerUpdate.as_view(), name='customer-form'),
    path('crm/customer/create/', views.CustomerCreate.as_view(), name='create-customer'),
    path('crm/lawn-mower/<int:pk>', views.LawnMowerDetailView.as_view(), name='mower-detail'),
    path('crm/lawn-mower/edit/<int:pk>', views.LawnMowerUpdate.as_view(), name='mower-form'),
    path('crm/lawn-mower/create/', views.LawnMowerCreate.as_view(), name='create-mower'),
    path('crm/lawn-mower/add/<int:custfk>', views.LawnMowerCreate.as_view(), name='add-mower'),
    path('crm/lawn-mower/service/edit/<int:pk>', views.ServiceRecordUpdate.as_view(), name='edit-service'),
    path('crm/lawn-mower/service/add/<int:mowerfk>', views.ServiceRecordCreate.as_view(), name='add-service'),
    path('hours/', views.hours, name='hours'),
]
