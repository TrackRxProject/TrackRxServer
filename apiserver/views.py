from django.shortcuts import render
from django.views.generic import View
# from django.contrib.auth.models import User, Group
# from models import Prescription, Dose
from django.http import HttpResponse
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from TrackRxServer.apiserver.serializers import UserSerializer,GroupSerializer
from django.views.decorators.csrf import csrf_exempt


class TestBottle(View):
    def get(self, request):
        return render(request, 'test_bottle.html')


class PrescriptionAPI(View):
    def get(self, request, uuid):
        # interval = Prescription.objects.get(uuid=uuid).interval
        interval = '02.50'
        return HttpResponse(interval, content_type='text/plain')

    @csrf_exempt
    def post(self, request, uuid):
        print uuid
        return HttpResponse('OK', content_type='text/plain')
