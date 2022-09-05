from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('',DiscountView.as_view(), name='discount'),
    path('course',DiscountCourseView.as_view(), name='discountCourse'),
    path('user',discountUserView.as_view(), name='discountCourse'),

]