from django.urls import path
from userapp import views

urlpatterns = [
    path('adspedia',views.index),
    path('login',views.login),
    
]

