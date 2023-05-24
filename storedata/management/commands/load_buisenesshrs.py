from csv import DictReader
from django.core.management import BaseCommand
from storedata.models import buisenessHour

class Command(BaseCommand):
    def handle(self, *args, **options):
        if buisenessHour.objects.exists():
            print('child data already loaded...exiting.')           
            return
        print("Loading buiseness hours data")

        for row in DictReader(open('./Menu hours.csv')):
            child=buisenessHour(storeId=row['store_id'], dayOfWeek=row['dayOfWeek'], startLocalTime=row['start_time_local'], endLocalTime=row['end_time_local'])  
            child.save()