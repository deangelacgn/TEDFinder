from django.conf.urls import url, include
from website.views import *
from django.conf.urls import handler404

handler404 = 'website.views.page_not_found'

urlpatterns = [
    # Auth
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^login/$', AuthView.as_view(), name='login_view'),
    url(r'^logout/$', LogoutView.as_view(), name='logout_view'),

    # Files
    url(r'^arquivos/$', DocumentView.as_view(), name='doc_view'),
    url(r'^arquivos/(?P<pk>[0-9]+)/delete/$', DocumentDelete.as_view(), name='doc_delete_view'),

    # Search
    url(r'^pesquisa/$', SearchView.as_view(), name='search_view'),
]
