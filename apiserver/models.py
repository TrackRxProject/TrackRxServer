from __future__ import unicode_literals

from django.db import models


class Prescription(models.Model):
    uuid = models.IntegerField()
    interval = models.CharField(max_length=5)
    activate = models.BooleanField()

    class Meta:
        db_table = "prescription"


class Adherence(models.Model):
    uuid = models.ForeignKey(Prescription)
    history = models.CharField(max_length=100)

    class Meta:
        db_table = "adherence"


class Info(models.Model):
    uuid = models.ForeignKey(Prescription)
    name = models.TextField()
    dosage = models.TextField()

    class Meta:
        db_table = "info"
