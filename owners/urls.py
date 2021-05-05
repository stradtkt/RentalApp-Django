from django.conf.urls import url
from . import views


app_name = 'owners'
urlpatterns = [
    url(r'^$', views.index, name='owners'),
]