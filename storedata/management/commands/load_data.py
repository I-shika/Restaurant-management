from csv import DictReader
from django.core.management import BaseCommand
from storedata.models import storeTimings

class Command(BaseCommand):
    def handle(self, *args, **options):
        if storeTimings.objects.exists():
            print('child data already loaded...exiting.')           
            return
        print("Loading childrens data")

        for row in DictReader(open('./store status.csv')):
            child=storeTimings(storeId=row['store_id'], timeStamp=row['timestamp_utc'], status=row['status'])  
            child.save()