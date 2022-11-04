from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.index, name='index'), 
    path('ohlc/', views.ohlc, name='ohlc'),
     path('ohlcform/', views.ohlcform, name='ohlcform'),
    path('formdata/', views.formdata, name='formdata'), 
    path('trade/', views.trade, name='trade'), 
    path('socket_data', views.socket_data, name='socket_data') 
]