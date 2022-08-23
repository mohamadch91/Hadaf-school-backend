from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
 path('archiveOfflineHeader/',ArchiveOfflineHeaderView.as_view(), name='archiveOfflineHeader'),
    path('archiveFiles/',ArchiveFilesView.as_view(), name='archiveFiles'),
]