"""TrackRxServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.conf.urls import include
# from rest_framework import routers
from TrackRxServer.apiserver import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
        url(r'^prescription/(?P<uuid>[0-9]+)/activate$',
            views.PrescriptionActivate.as_view()),
        url(r'^prescription/(?P<uuid>[0-9]+)/interval$',
            views.PrescriptionInterval.as_view()),
        url(r'^info/(?P<uuid>[0-9]+)$', views.InfoView.as_view()),
        url(r'^adherence/(?P<uuid>[0-9]+)$', views.AdherenceView.as_view()),
        url(r'^notify/(?P<uuid>[0-9]+)$', views.InfoView.as_view()),
]
