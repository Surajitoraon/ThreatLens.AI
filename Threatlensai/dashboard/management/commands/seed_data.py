from django.core.management.base import BaseCommand
from dashboard.models import PhishingLog, MalwareLog
from flask_celery import Faker
import random

class Command(BaseCommand):
    help = "Seed database with fake threat logs"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            PhishingLog.objects.create(
                subject=fake.sentence(),
                body=fake.text(),
                risk_score=random.randint(0, 5),
                is_phishing=random.choice([True, False])
            )
        for _ in range(10):
            MalwareLog.objects.create(
                filename=fake.file_name(),
                malware_detected=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS("Fake data added!"))
