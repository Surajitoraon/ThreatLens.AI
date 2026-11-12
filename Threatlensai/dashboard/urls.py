from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("phishing_scan/", views.phishing_scan),
    path("malware_scan/", views.malware_scan),
    path("stats/", views.stats),
    path("attack_feed/", views.attack_feed),
]
