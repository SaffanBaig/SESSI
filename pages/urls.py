from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='pages_home'),
    path('about',views.about, name='pages_about'),
    path('contact',views.contact, name='pages_contact'),
]