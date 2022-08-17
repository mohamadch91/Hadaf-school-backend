from django.urls import path
from .views import *

urlpatterns = [
    path('grade/', gradeView.as_view(), name='grade'),
    path('department/',departmentView.as_view(), name='department'),
    path('lesson/', lessonsView.as_view(), name='lesson'),
    path('days/',daysView.as_view(), name='days'),
     path('year/',yearView.as_view(), name='year'),
     path('course/',CourseTypeView.as_view(), name='course'),
    
]
#salam