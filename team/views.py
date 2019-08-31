from django.shortcuts import render
from .models import Team, Seniority

def members(request):
    team = Team.objects.all()
    context = {
        'teams':team
    }
    return render(request, "team/home.html", context)

def committee(request):
    return render(request,"team/committee.html")

def org_chart(request):
    return render(request,"team/org.html")

def seniority(request):
    seniority = Seniority.objects.all()
    context = {
        'senioritys':seniority
    }
    return render(request, "team/seniority.html", context)
