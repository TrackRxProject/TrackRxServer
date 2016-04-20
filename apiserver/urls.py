from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import PrescriptionViewSet, AdherenceViewSet, InfoViewSet
# from rest_framework import renderers
from views import PrescriptionActivate


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

notify = InfoViewSet.as_view({
    'get': 'prescription_info',
    'put': 'set_info'
})

urlpatterns = [
    url(r'^prescription/(?P<uuid>[0-9]+)/interval$', prescription_list),
    url(r'^prescription/(?P<uuid>[0-9]+)/activate$',
        PrescriptionActivate.as_view()),
    # url(r'^adherence/(?P<uuid>[0-9]+)$', adherence),
    url(r'^notify/(?P<uuid>[0-9]+)$', notify),
    url(r'^info/(?P<uuid>[0-9]+)$', info),
]

urlpatterns = format_suffix_patterns(urlpatterns)
