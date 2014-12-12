import logging
from django.conf.urls import patterns, include, url
from django.contrib import admin

log = logging.getLogger(__name__)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'coopbox_base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'coopbox_base.views.index.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'calendar/', include('calendarium.urls')),
)

log.error('ho')
