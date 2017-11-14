from django.conf.urls import url, include
from website.views import *
from django.conf.urls import handler404

handler404 = 'website.views.page_not_found'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'estacionamento/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})/$', PLGeneralPermissionUpdateView.as_view(), name='parking_lot_update_view'),
]