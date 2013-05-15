# Django specific
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

# App specific
from simple_sso.sso_client.client import Client

admin.autodiscover()
sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = patterns('',
    url(r'^auth/', include(sso_client.get_urls())),
    url(r'^admin/', include(admin.site.urls)),
)