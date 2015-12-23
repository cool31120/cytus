from django.conf.urls import url
from record import views


urlpatterns = [
    url(r'^$', views.record, name='record'),
]