from django.conf.urls import url
from story import views


urlpatterns = [
    url(r'^$', views.story, name='story'),
]