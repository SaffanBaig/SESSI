from django.shortcuts import render


def functions(request):
    context = {
        "title" : "Our Functions",
        "desc": "Our function is to provide medical care and cash benefits to secured workers and their dependants"
    }
    return render(request,"services/function.html", context)


def medicalServices(request):
    context = {
        "title":"Medical Services",
        "desc":"We provide 24/7 medical services to our members"
    }
    return render(request,"services/medical.html", context)

def hospitals(request):
    return render(request,"services/hospitals.html")

def proj(request):
    context = {
        "title":"Our Projects",
        "desc":"Sessi is continuously working on betterment of hospitals in Sindh"
    }
    return render(request,"services/project.html", context)

def cashBenefits(request):
    return render(request, "services/cash.html")

