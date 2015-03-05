from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'', include('gmapi.urls.media')), # Use for debugging only.
    (r'^$', 'myapp.views.index'),
)