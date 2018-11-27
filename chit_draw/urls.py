from django.conf.urls import url
from .views import chitdraw, delete_chit_details

app_name = 'chit_draw'
urlpatterns = [
    url(r'^$', chitdraw, name='ChitInstallmentForm'),
    url(r'^delete_chit_details/(?P<pk>\d+)$', delete_chit_details, name='delete_chit_details'),
]
