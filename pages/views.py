from django.shortcuts import render

def home(request):
    # superusers = User.objects.filter(is_superuser=True)
    # context = {
    #     "superuser":superusers
    # }
    return render(request, "pages/home.html")

def about(request):
    context = {
        "title":"About Us",
        "desc":"lorem15"
    }
    return render(request, "pages/about.html", context)

def contact(request):
    context = {
        "title":"Contact Us",
        "desc":"email:info@sessi.gov.pk"
    }
    return render(request, "pages/contact.html", context)
