from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('discount/',DiscountView.as_view(), name='discount'),
    path('discountCourse/',DiscountCourseView.as_view(), name='discountCourse'),
]