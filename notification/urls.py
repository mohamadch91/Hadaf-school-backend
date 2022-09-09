from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('',notificationView.as_view(), name='notification'),
    path('student/',studentNotificationView.as_view(), name='studentNotification'),
]