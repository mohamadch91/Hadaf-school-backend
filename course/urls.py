from django.urls import path
from .views import *

urlpatterns = [

     path('course/',courseView.as_view(), name='course'),
    
]