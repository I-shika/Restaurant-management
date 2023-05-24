from django.urls import path
from .views import triggerReport

urlpatterns=[

path('importdata', triggerReport)
]