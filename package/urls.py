from django.urls import path
from .views import *

urlpatterns = [
    path('normalPackage', normalPackageView.as_view()),
    path('normalPackageCourse', normalPackageCourseView.as_view()),
    path('timingPackage', timingPackageView.as_view()),
    path('timingPackageCourse', timingPackageCourseView.as_view()),
    path('studentPackage', studentPackageView.as_view()),
    path('studentPackageCourse', studentPackageCourseView.as_view()),
    path('studentPackageDiscount', studentPackageDiscountView.as_view()),

]

