# Django specific
from django.conf.urls import patterns, include, url
from django.contrib import admin

# App specific
from simple_sso.sso_server.server import Server

admin.autodiscover()
authserver = Server()

urlpatterns = patterns('',
    url(r'^authserver/', include(authserver.get_urls())),
    url(r'^admin/', include(admin.site.urls)),
)