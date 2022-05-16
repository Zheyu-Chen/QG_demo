from django.urls import path

from FAQ.views import *

urlpatterns = [
    path('FAQ_page', FAQ_page, name="FAQ_page"),
]