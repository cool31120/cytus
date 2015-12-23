from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^wiki/', include('wiki.urls', namespace='wiki')),
    url(r'^story/', include('story.urls', namespace='story')),
    url(r'^record/', include('record.urls', namespace='record')),
    url(r'^.*', include('main.urls')),
]
