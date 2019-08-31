from django.shortcuts import render
from .models import Ad

def ads(request):
    ad = Ad.objects.all()
    context = {
        'ads' : ad
    }
    return render(request, "ads/ads.html", context)

