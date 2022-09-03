from django.urls import path
from .views import *

urlpatterns = [

    path('',dahsboardVIew.as_view(), name='course'),
    path('admin',admindahsboardVIew.as_view(), name='course'),


]
