from django.urls import path, include
from . import views

urlpatterns = [
    
    path("about/", views.about_page, name="about"),
    path("contact/", views.contact_page, name="contact"),
    path("cources/", views.cources_page, name="cources"),
    path("", views.index_page, name="index"),
    path("team/", views.team_page, name="team")
    
]
