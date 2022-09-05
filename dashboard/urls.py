from django.urls import path
from .views import *

urlpatterns = [

    path('',dahsboardVIew.as_view(), name='course'),
    path('admin',admindahsboardVIew.as_view(), name='course'),
    path('wallet',walletView.as_view(), name='course'),
    path('basket',basketView.as_view(), name='course'),


]
