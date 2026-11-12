from django.shortcuts import render
from django.http import JsonResponse
from .models import PhishingLog, MalwareLog
from .utils.attack_sim import generate_attack
import random

def index(request):
    return render(request, "dashboard/index.html")

def phishing_scan(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        suspicious_keywords = ["urgent", "password", "click here", "verify"]
        score = sum(word in body.lower() for word in suspicious_keywords)
        is_phishing = score > 2
        log = PhishingLog.objects.create(subject=subject, body=body,
                                         risk_score=score, is_phishing=is_phishing)
        return JsonResponse({"risk_score": score, "is_phishing": is_phishing})

def malware_scan(request):
    if request.method == "POST":
        file = request.FILES["file"]
        log = MalwareLog.objects.create(filename=file.name, malware_detected=False)
        return JsonResponse({"filename": file.name, "malware_detected": False})

def stats(request):
    return JsonResponse({
        "phishing": PhishingLog.objects.count(),
        "malware": MalwareLog.objects.count()
    })

def attack_feed(request):
    attack = generate_attack()
    return JsonResponse(attack)
