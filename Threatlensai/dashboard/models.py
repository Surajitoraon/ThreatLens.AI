# pyright: reportMissingImports=false
from django.db import models

class PhishingLog(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    risk_score = models.IntegerField()
    is_phishing = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

class MalwareLog(models.Model):
    filename = models.CharField(max_length=200)
    malware_detected = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
