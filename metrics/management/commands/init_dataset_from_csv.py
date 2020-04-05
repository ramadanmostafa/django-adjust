import csv
from datetime import datetime

from django.core.management import BaseCommand

from metrics.models import DataSet


class Command(BaseCommand):
    help = 'Init DataSet model from csv.'

    def handle(self, *args, **options):
        reader = csv.DictReader(open('data.csv'), delimiter=',')
        for row in reader:
            DataSet.objects.create(
                date=datetime.strptime(row.get('date').strip(), '%Y-%m-%d'),
                channel=row.get('channel').strip(),
                country=row.get('country').strip(),
                os=row.get('os').strip(),
                impressions=row.get('impressions').strip(),
                clicks=row.get('clicks').strip(),
                spend=row.get('spend').strip(),
                revenue=row.get('revenue').strip(),
                installs=row.get('installs').strip()
            )
