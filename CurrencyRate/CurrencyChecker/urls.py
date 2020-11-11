from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main_page'),  # Main page url, where chart will be show
    path('add_currency/', views.add_currency_page, name='add_currency_page'),  # Page for adding new currency rate
]
