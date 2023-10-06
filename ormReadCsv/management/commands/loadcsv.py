import csv
from django.core.management.base import BaseCommand
from ormReadCsv.models import CSVRecord

class Command(BaseCommand):
    help = 'Load data from a CSV file into the CSVRecord model'

    def handle(self, *args, **options):
        csv_file_path = 'industry.csv'  # Replace with the path to your CSV file

        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                CSVRecord.objects.create(**row)