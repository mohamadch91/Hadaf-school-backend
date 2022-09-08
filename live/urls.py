from django.urls import path
from .views import *

urlpatterns = [
 path('create/',liveView.as_view(), name='forumHeader'),
    path('join/',joinView.as_view(), name='forumHeader'),
    path('student_join/',student_joinView.as_view(), name='forumHeader'),
    path('getmeetings',getMeetings.as_view(), name='forumHeader'),
]
  