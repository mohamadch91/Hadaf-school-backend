from django.urls import path
from .views import *

urlpatterns = [
    path('', SliderView.as_view(), name='slider'),
    path('banner',BannerView.as_view(), name='banner'),
]
#salam