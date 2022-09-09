from django.urls import path
from .views import *

urlpatterns = [

    path('course/',courseView.as_view(), name='course'),
    path('studentCourse/',studentCourseView.as_view(), name='studentCourse'),
    path('courseHomeWork/', CourseHomeWorkView.as_view(), name='courseHomeWork'),
    path('courseDays/',CourseDaysView.as_view(), name='courseDaysType'),
    path('courseType/',CourseTypeView.as_view(), name='courseType'),
    path('teacherCourse/',teacherCourse.as_view(), name='teacher courses'),
    path('coursehw/',coursegetHomeVIew.as_view(), name=' courses hw'),
    path('specificstudentCourse/',specifiecStudentcourse.as_view(),name="student course"),
    path('block/',blockstudents.as_view(),name="student course"),
    path('courseStudent/',specificCoourseSes.as_view(),name="student course"),
    path('teacherScount/',teacherStudensView.as_view(),name="student course"),
    path('bulkimport/',bulkstudentView.as_view(),name="student course"),







]
