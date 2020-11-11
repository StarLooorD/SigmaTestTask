from django.contrib import admin
from django.urls import path, include
from .views import redirect_main

urlpatterns = [
    path('', redirect_main),  # Redirecting to main page automatically
    path('admin/', admin.site.urls),  # Django admin page
    path('currency_checker/', include('CurrencyChecker.urls')),  # Redirecting to our app urls
]
