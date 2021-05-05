from django.conf.urls import url
from . import views


app_name = 'properties'
urlpatterns = [
    url(r'^$', views.index, name='properties'),
]