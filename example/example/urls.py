# Django specific
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse

# App specific
from simple_sso.sso_server.server import Server

admin.autodiscover()
admin.site.login = login_required(admin.site.login, login_url=reverse_lazy(settings.LOGIN_URL))

authserver = Server()

urlpatterns = patterns('',
    url(r'^authserver/', include(authserver.get_urls())),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'
    }, name='login'),
)

# App mock
urlpatterns += patterns('',
    url('^$', lambda request: HttpResponse('Welcome at the <strong>server</strong> visit <a href="/secret/">secret</a> or <a href="/admin/">admin</a>.')),
    url('^secret/$', login_required(
        lambda request: HttpResponse('Secret at the server'),
        login_url=reverse('login')
    ), name='root'),
)