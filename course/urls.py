from django.urls import path
from .views import *

urlpatterns = [

    path('course/',courseView.as_view(), name='course'),
    path('studentCourse/',studentCourseView.as_view(), name='studentCourse'),
    path('courseHomeWork/', CourseHomeWorkView.as_view(), name='courseHomeWork'),
    path('courseDays/',CourseDaysView.as_view(), name='courseDaysType'),
    path('courseType/',CourseTypeView.as_view(), name='courseType'),
    path('archiveOfflineHeader/',ArchiveOfflineHeaderView.as_view(), name='archiveOfflineHeader'),
    path('archiveFiles/',ArchiveFilesView.as_view(), name='archiveFiles'),
    path('discount/',DiscountView.as_view(), name='discount'),
    path('discountCourse/',DiscountCourseView.as_view(), name='discountCourse'),
]
