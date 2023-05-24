from django.contrib import admin
from .models import storeTimings,buisenessHour,timezone


class storeTimingsAdmin(admin.ModelAdmin):
   list_display=('storeId','timeStamp','status')

class buisenessHourAdmin(admin.ModelAdmin):
   list_display=('storeId','dayOfWeek','startLocalTime','endLocalTime')

class timezoneAdmin(admin.ModelAdmin):
   list_display=('storeId','timezone')



# Register your models here.
admin.site.register(storeTimings,storeTimingsAdmin)
admin.site.register(buisenessHour, buisenessHourAdmin)
admin.site.register(timezone,timezoneAdmin)