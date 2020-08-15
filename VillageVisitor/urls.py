from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('Take_Response/',views.Take_Response, name='Take_Response'),
]