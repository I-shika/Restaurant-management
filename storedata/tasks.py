from celery import shared_task


@shared_task()
def create_report():
   print('hello')

