from django.contrib.auth.models import User, Group
from models import Prescription, Dose

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = ('uuid')


class Prescription(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('uuid')
