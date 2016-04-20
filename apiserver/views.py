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
from rest_framework.decorators import parser_classes
from rest_framework.parsers import BaseParser


import requests
import json

class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        data = stream.read()
        for x in data:
            print "Adherence = " + x
        return stream.read()


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

    parser_classes = (PlainTextParser,)

    @csrf_exempt
    def put(self, request, uuid):
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
    def post(self, request, uuid):
        url = 'https://gcm-http.googleapis.com/gcm/send'
        headers = {'Authorization': 'key=AIzaSyArADgdOmRwMRFzsSj9p4G7c0U0cdW8reM',
                   'Content-Type': 'application/json'}
        payload = {
            "data": {
                "info": {
                    "subject": "Medication Reminder",
                    "message": "Time to take your medication",
                }
            },
            "to" : "cIXiqCIanRg:APA91bEazp38G7yzsf8xXcrzdVgUCvr7PauD96jvv9VpDNl1aY2ePa-8E8by7tq6lo956YED2foLCNbHHuqcT8sqyU5ZyYeUcbDMKQcyfeTgvnekgzAZqcIh974dW30l3tWkLmm2sqp7"
        }

        requests.post(url, headers=headers, data=json.dumps(payload))

        return HttpResponse('OK', status=201)

    def get(self, request, uuid):
        print uuid
        inf = Info.objects.get(uuid=uuid)
        serializer = InfoSerializer(inf)
        return Response(serializer.data)

