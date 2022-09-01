from django.urls import path
from .views import *

urlpatterns = [
    path('list', smsList.as_view(), name='smsList'),
]
#salam