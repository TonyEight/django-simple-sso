# Django specific
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse

# App specific
from simple_sso.sso_client.client import Client

admin.autodiscover()
sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

urlpatterns = patterns('',
    url(r'^auth/', include(sso_client.get_urls())),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'
    }, name='login'),
)

# App mock
urlpatterns += patterns('',
    url('^$', login_required(
        lambda request: HttpResponse('Secret at the client'),
        login_url=reverse('login')
    ), name='root'),
)