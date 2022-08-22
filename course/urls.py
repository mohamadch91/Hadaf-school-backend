from django.urls import path
from .views import *

urlpatterns = [

    path('course/',courseView.as_view(), name='course'),
    path('studentCourse/',studentCourseView.as_view(), name='studentCourse'),
    path('courseHomeWork/', CourseHomeWorkView.as_view(), name='courseHomeWork'),

]
