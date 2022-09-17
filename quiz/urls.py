from django.urls import path
from .views import *

urlpatterns = [
 path('quizHeader/',quizHeaderView.as_view(), name='quizHeader'),
    path('quizQuestion/',quizQuestionView.as_view(), name='quizQuestion'),
        path('studentQueez/',studentQueezView.as_view(), name='studentQueez'),
        path('studentres/',studentResult.as_view(), name='studentQueez'),
        path('tstudentres/',totalStudentResult.as_view(), name='studentQueez'),

        path('totalqH/',totalquizHeaderView.as_view(), name='studentQueez'),
        path('totalqS/',totalquizSubjectsView.as_view(), name='studentQueez'),
        path('totalqQ/',totalquizQuestionsView.as_view(), name='studentQueez'),
        path('totalqSu/',totalstudentQueezView.as_view(), name='studentQueez'),


]