from django.urls import path
from .views import *

urlpatterns = [
 path('forumHeader/',ForumHeaderView.as_view(), name='forumHeader'),
    path('forumDetail/',ForumDetailView.as_view(), name='forum Detail'),
]