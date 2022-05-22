from django.urls import path

from . import views

urlpatterns = [
    path('',views.getCustomerInformation,name='getCustomerInformation')
]