from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User, Group
from models import Prescription, Dose
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from TrackRxServer.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TestBottle(View):
    def get(self, request):
        return render(request, 'test_bottle.html')


# @api_view(['GET'])
def prescription_interval(request, uuid):
    interval = Prescription.objects.get(uuid=uuid).interval
    return HttpResponse(interval, content_type='text/plain')
