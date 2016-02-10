# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Prescription
from models import Adherence
from models import Info
from serializers import PrescriptionSerializer
from serializers import AdherenceSerializer
from serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView


class PrescriptionActivate(APIView):

    @csrf_exempt
    def post(self, request, uuid):
        print uuid
        pres = Prescription.objects.get(uuid=uuid)
        ser = PrescriptionSerializer(pres, data={'activate': True},
                                     partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        # return HttpResponse('OK', content_type='text/plain')

    def get(self, request, uuid):
        print uuid
        pres = Prescription.objects.get(uuid=uuid)
        serializer = PrescriptionSerializer(pres)
        # return Response(serializer.data.get('activate'))
        return Response(serializer.data)

    '''
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def interval(self, request, uuid):
        # interval = Prescription.objects.get(uuid=uuid).interval
        print uuid
        # interval = '02.50'
        # return HttpResponse(interval, content_type='text/plain')
    '''


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
