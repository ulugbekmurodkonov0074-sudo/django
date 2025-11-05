from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def contact_page(request):
    return render(request, "contact.html")

def cources_page(request):
    return render(request, "cources.html")

def team_page(request):
    return render(request, "team.html")
    path("", views.home_page, name="home"),
    
def about_page(request):
    return render(request, "about.html")

def views_page(request):
    return render(request, "views.html")
