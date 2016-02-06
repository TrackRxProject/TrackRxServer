from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Patient(models.Model):
    uuid = models.IntegerField()

    class Meta:
        db_table = "patient"


class Prescription(models.Model):
    uuid = models.ForeignKey(Patient)
    interval = models.IntegerField()

    class Meta:
        db_table = "prescription"


class Dose(models.Model):
    prescription = models.ForeignKey(Prescription)
    uuid = models.IntegerField()

    class Meta:
        db_table = "dose"
