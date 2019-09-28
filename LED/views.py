from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .LED_controller.controller import LedController

class LedControllerOn(View):

    def get(self, request):
        LedController().on()
        return HttpResponse('on')

class LedControllerOff(View):

    def get(self, request):
        LedController().off()
        return HttpResponse('off')

