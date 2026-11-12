from django.core.management.base import BaseCommand
from dashboard.models import PhishingLog, MalwareLog
import datetime
import random

COUNTRIES = [
    "United States", "Canada", "Germany", "France", "Australia",
    "Brazil", "India", "Japan", "United Kingdom", "Netherlands"
]

CITIES = [
    "New York", "Toronto", "Berlin", "Paris", "Sydney",
    "São Paulo", "Mumbai", "Tokyo", "London", "Amsterdam"
]

def random_ipv4_public():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def generate_attack():
    return {
        "ip": random_ipv4_public(),
        "country": random.choice(COUNTRIES),
        "city": random.choice(CITIES),
        "type": random.choice(["phishing", "malware", "ddos"]),
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
