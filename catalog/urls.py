from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.ServiceTypeListView.as_view(), name='services'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('about-us/', views.aboutus, name='about-us'),
    path('for-sale/', views.ForSaleListView.as_view(), name='for-sale'),
    path('for-sale/<int:pk>', views.ForSaleDetailView, name='forsale-detail'),
]
