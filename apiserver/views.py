from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Prescription
from models import Adherence
from models import Info
from serializers import PrescriptionSerializer
from serializers import AdherenceSerializer
from serializers import InfoSerializer
from rest_framework.response import Response
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

    def get(self, request, uuid):
        print uuid
        pres = Prescription.objects.get(uuid=uuid)
        serializer = PrescriptionSerializer(pres)
        # return Response(serializer.data.get('activate'))
        return Response(serializer.data)


class PrescriptionInterval(APIView):
    def get(self, request, uuid):
        interval = Prescription.objects.get(uuid=uuid).interval
        print uuid
        return HttpResponse(interval, content_type='text/plain')


class AdherenceView(APIView):
    @csrf_exempt
    def post(self, request, uuid):
        print request.data
        # "bitvector" logic here
        return HttpResponse('OK', status=201)

    def get(self, request, uuid):
        print uuid
        adh = Adherence.objects.get(uuid=uuid)
        serializer = AdherenceSerializer(adh)
        return Response(serializer.data)


class InfoView(APIView):
    @csrf_exempt
    def put(self, request, uuid):
        print request.data
        # add new info to db
        return HttpResponse('OK', status=201)

    def get(self, request, uuid):
        print uuid
        inf = Info.objects.get(uuid=uuid)
        serializer = InfoSerializer(inf)
        return Response(serializer.data)
