from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmallEngineClassView, name='classes'),
    path('unsubscribe/<str:email>', views.Unsubscribe, name='unsub'),
    path('updateemaillist/', views.UpdateEmailList, name='UpdateEmailList')
]
