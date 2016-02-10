# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Prescription, Adherence, Info
from serializers import PrescriptionSerializer, AdherenceSerializer
from serializers import InfoSerializer
# from rest_framework.response import Response
from rest_framework import viewsets


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def interval(self, request, uuid):
        # interval = Prescription.objects.get(uuid=uuid).interval
        print uuid
        # interval = '02.50'
        # return HttpResponse(interval, content_type='text/plain')

    @csrf_exempt
    def activate(self, request, uuid):
        print uuid
        # return HttpResponse('OK', content_type='text/plain')

    def is_activated(self, request, uuid):
        print uuid


class AdherenceViewSet(viewsets.ModelViewSet):
    queryset = Adherence.objects.all()
    serializer_class = AdherenceSerializer

    @csrf_exempt
    def update_adherence(self, request, uuid):
        print uuid
        # print request.POST.get('uuid')

    def adhr_history(self, request, uuid):
        print uuid


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

    @csrf_exempt
    def set_info(self, request, uuid):
        print uuid

    def prescription_info(self, request, uuid):
        print "hi!"
        print uuid
