# Django specific
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse

# App specific
from simple_sso.sso_server.server import Server

admin.autodiscover()
admin.site.login = login_required(admin.site.login, login_url=reverse_lazy('login'))

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
    url('^$', login_required(
        lambda request: HttpResponse('Secret at the server'),
        login_url=reverse('login')
    ), name='root'),
)