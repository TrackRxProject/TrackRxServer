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

        return data


class PrescriptionActivate(APIView):

    @csrf_exempt
    def post(self, request, uuid):
        print uuid
        pres = Prescription.objects.get(uuid=uuid)
        ser = PrescriptionSerializer(pres, data={'activate': True, 'reset': False},
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

    # /pin/<uuid>/
    @csrf_exempt
    def post(self, request, uuid):
        print "Here"
        print request.data
        print Info.objects.get(uuid=uuid).pin

        if request.data['pin'] == Info.objects.get(uuid=uuid).pin:
            p = Prescription.objects.get(uuid=uuid)
            p.auth = True
            p.save()

        return HttpResponse('OK', status=201)


class AdherenceView(APIView):

    parser_classes = (PlainTextParser,)

    @csrf_exempt
    def put(self, request, uuid):
        # TODO: logic for calculating which day?
        for adh in request.data:
            p = Prescription.objects.get(uuid=uuid)
            if adh == '1':
                a = Adherence(uuid=p, history=1)
            else:
                a = Adherence(uuid=p, history=0)
            a.save()

        return HttpResponse('OK', status=201)

    # /adherence/<uuid>
    def get(self, request, uuid):
        adherences = Adherence.objects.filter(uuid_id=uuid)
        histories = []
        for adh in adherences:
            histories.append(adh.history)

        retval = json.dumps(histories)

        return HttpResponse(retval, status=201)

class InfoView(APIView):
    # /notify/1
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


class AuthView(APIView):
    def get(self, request, uuid):
        retval = ""
        print Prescription.objects.get(uuid=uuid).auth
        if Prescription.objects.get(uuid=uuid).auth:
            retval = "1"
            p = Prescription.objects.get(uuid=uuid)
            p.auth = False
            p.save()
        else:
            retval = "0"

        return HttpResponse(retval, content_type='text/plain')


class ResetView(APIView):
    def get(self, request, uuid):
        if Prescription.objects.get(uuid=uuid).reset:
            return HttpResponse("1", content_type='text/plain')
        else:
            return HttpResponse("0", content_type='text/plain')


    @csrf_exempt
    def put(self, request, uuid):
        p = Prescription.objects.get(uuid=uuid)
        if not p.reset:
            p.reset = True
            p.save()
            return HttpResponse('RESET', status=201)
        else:
            return HttpResponse('NOTRESET', status=201)

