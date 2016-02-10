from models import Prescription, Adherence, Info

from rest_framework import serializers


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('uuid', 'interval', 'activate')


class AdherenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adherence
        fields = ('uuid', 'history')


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('uuid', 'name', 'dosage')
