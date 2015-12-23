from django.conf.urls import url
from wiki import views


urlpatterns = [
    url(r'^$', views.wiki, name='wiki'),
    url(r'^category/(?P<categoryID>[0-9]+)/$', views.category, name='category'),
]