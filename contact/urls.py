from django.urls import path

from contact.views import *

app_name = 'contact'

urlpatterns = [
    path('contact-form', ContactView.as_view(), name='contact-form'),
    path('contact-success', ContactSuccessView.as_view(), name='contact-success'),
]
