from django.conf.urls.defaults import *
from django.contrib import admin

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality to
# the project's homepage.
urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    ("^news/", include("news.urls")),
    ("^", include("mezzanine.urls")),
)

#if settings.DEBUG and not settings.DEV_SERVER:
#    urlpatterns = patterns('',
#        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    ) + urlpatterns
