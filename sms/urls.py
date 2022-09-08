from django.urls import path
from .views import *

urlpatterns = [
    path('list', smsList.as_view(), name='smsList'),
    path('last', lastsms.as_view(), name='smsList'),
    path('send_bulk', send_bulks.as_view(), name='smsList'),


]
#salam