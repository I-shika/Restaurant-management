from csv import DictReader
from django.core.management import BaseCommand
from storedata.models import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        if timezone.objects.exists():
            print('child data already loaded...exiting.')           
            return
        print("Loading childrens data")

        for row in DictReader(open('./timezone.csv')):
            child=timezone(storeId=row['store_id'],timezone=row['timezone_str'])
            child.save()