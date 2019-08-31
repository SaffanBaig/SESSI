from django.urls import path

from . import views

urlpatterns = [
    path('medical',views.medicalServices, name='servicesmedical'),
    path('projects',views.proj, name='servicesproj'),
    path('hospitals',views.hospitals, name='serviceshospitals'),
    path('functions',views.functions, name='servicesfunctions'),
    path('cashbenefits',views.cashBenefits, name='servicescash'),

]