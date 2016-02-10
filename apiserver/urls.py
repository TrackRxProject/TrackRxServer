from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import PrescriptionViewSet, AdherenceViewSet, InfoViewSet
# from rest_framework import renderers


prescription_list = PrescriptionViewSet.as_view({
    'get': 'interval',
})

prescription_activate = PrescriptionViewSet.as_view({
    'get': 'is_activated',
    'put': 'activate',
})

adherence = AdherenceViewSet.as_view({
    'post': 'update_adherence',
    'get': 'adhr_history',
})

info = InfoViewSet.as_view({
    'get': 'prescription_info',
    'put': 'set_info'
})

urlpatterns = [
    url(r'^prescription/(?P<uuid>[0-9]+)/interval$', prescription_list),
    url(r'^prescription/(?P<uuid>[0-9]+)/activate$', prescription_activate),
    url(r'^adherence/(?P<uuid>[0-9]+)$', adherence),
    url(r'^info/(?P<uuid>[0-9]+)$', info),
]

urlpatterns = format_suffix_patterns(urlpatterns)
