# Github.com/Rasooll
from django.urls import path
from .views import *

urlpatterns = [
    # path('request/', views.send_request, name='request'),
    # path('verify/', views.verify , name='verify'),
    path('buywallet/', buyWalletView.as_view() , name='verify'),

]
