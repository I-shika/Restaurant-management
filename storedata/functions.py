from .serializer import storeTimingsSerializer, timezoneSerializer
from .models import storeTimings, timezone, buisenessHour
import datetime

# for accessing the data


#  storeId=storeTimings.objects.all()
        
#         for i in storeId:
#            storedata=storeTimingsSerializer(storeId,many=True)
#            data= storedata.data
#            print(data)
#            Id=timezone.objects.filter(storeId=i).all()
#            timingdata= timezoneSerializer(Id,many=True)
#            time=timingdata.data
#            print(time)

def accessData():
        
        storeId=storeTimings.objects.all()[:200]
        data=[]
        time=[]
        for i in storeId:
           storedata=storeTimingsSerializer(i)
           data.append(storedata.data)
           Id=timezone.objects.filter(storeId=i).values()
           timingdata= timezoneSerializer(Id,many=True)
           time.append(timingdata.data) 
           points = [{ "data" : data , "time" : time}]
        return(points)

# def lastHourUptime( lastUpdatedTime,weekday):
#     nowDatetime = datetime.datetime.now()
#     todayWeekDay = nowDatetime.weekday()
#     oneHourBefore = nowDatetime - datetime.timedelta(hours=1)
#     oneDayBefore = nowDatetime-datetime.timedelta(days=1)
#     oneWeekBefore= nowDatetime-datetime.timedelta(days=7)
#     if(lastUpdatedTime<oneHourBefore):
#         return 'Updated'
#     elif(lastUpdatedTime>oneHourBefore):
#         current_datetime = last_updated_datetime
        
#     for i in weekday:
#         if(i==todayWeekDay):
#             openingHour=
      
      