from django.urls import path
from LED.views import LedControllerOn, LedControllerOff

urlpatterns = [
    path('on', LedControllerOn.as_view(), name="on"),
    path('off', LedControllerOff.as_view(), name="off"),
]