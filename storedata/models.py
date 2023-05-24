from django.db import models
from django.utils import timezone
import datetime


class storeTimings(models.Model):
    storeId=models.CharField(max_length=100, verbose_name='storeId')
    timeStamp=models.CharField(verbose_name='timeStamp',max_length=50)
    status = models.CharField(max_length=10, verbose_name='status')
    
    def __str__(self):
        return self.storeId
    class Meta:
        """
        Meta class for Doctor
        """
        verbose_name_plural = "storeTimings"
    

class buisenessHour(models.Model):
  storeId=models.CharField(max_length=100, verbose_name='storeId')
  dayOfWeek=models.CharField(max_length=10, verbose_name='dayOfWeek')
  startLocalTime = models.CharField(max_length=20, verbose_name='startLocalTime')
  endLocalTime = models.CharField(max_length=20, verbose_name='endLocalTime')

  def __str__(self):
        return self.storeId, self.dayOfWeek, self.startLocalTime, self.endLocalTime
  
class timezone(models.Model):
    storeId=models.CharField(max_length=100, verbose_name='storeId')
    timezone=models.CharField(max_length=50,verbose_name='timezone')
    
    def __str__(self):
        return self.storeId, self.timezone

class Report(models.Model):
    storeId=models.CharField(max_length=100, verbose_name='storeId')
    uptimeLastHour=models.CharField(max_length=100, verbose_name='uptimeLastHour')
    uptimeLastDay=models.CharField(max_length=100, verbose_name='uptimeLastHour')
    uptimeLastWeek=models.CharField(max_length=100, verbose_name='uptimeLastWeek')
    downtimeLastHour=models.CharField(max_length=100, verbose_name='downtimeLastHour')
    downtimeLastDay=models.CharField(max_length=100, verbose_name='downtimeLastDay')
    downtimeLastWeek=models.CharField(max_length=100, verbose_name='downtimeLastWeek')
    reportId=models.CharField(max_length=100, verbose_name='reportId')
    status = models.CharField(max_length=20,default=False, verbose_name='status')
    
    def __str__(self):
        return self.storeId
    
    def save(self,*args, **kwargs):
         if not self.reportId:
          self.reportId= id
         return super(Report, self).save(*args, **kwargs)
    


