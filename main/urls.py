from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home_page'),
    path('parse', alldata, name='result_page'),
]