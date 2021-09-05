from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from portfolio.views import *

app_name = 'portfolio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('', HomePageView.as_view(), name="home"),
]
