from django.conf.urls import url, include
from website.views import *
from django.conf.urls import handler404

handler404 = 'website.views.page_not_found'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^login/$', AuthView.as_view(), name='login_view'),
    url(r'^logout/$', LogoutView.as_view(), name='logout_view'),
    url(r'^arquivos/$', DocumentView.as_view(), name='doc_view'),
    url(r'^arquivos/(?P<pk>[0-9]+)/delete/$', DocumentDelete.as_view(), name='doc_delete_view'),
    # url(r'estacionamento/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})/$', PLGeneralPermissionUpdateView.as_view(), name='parking_lot_update_view'),
]
