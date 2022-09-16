# Github.com/Rasooll
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
    path('buywallet/', buyWalletView.as_view() , name='verify'),
    path('buybasket/', addTowallet.as_view() , name='verify'),
    path('report/', report.as_view() , name='verify'),
    path('add/', addbuy.as_view() , name='verify'),

    

]
