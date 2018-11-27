from django.conf.urls import url
from .views import chitrequest

app_name = 'chit_request'
urlpatterns = [
    url(r'^$', chitrequest, name='chit_request'),

]
