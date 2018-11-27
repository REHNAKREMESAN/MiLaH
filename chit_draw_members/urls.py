from .views import chit_draw_memb, delete_chit_details
from django.conf.urls import url

app_name = 'chit_draw_members'
urlpatterns = [
    url(r'^chit_memb/(?P<pk>\d+)$', chit_draw_memb, name='chit_draw_memb'),
    url(r'^delete_chit_details/(?P<pk>\d+)$', delete_chit_details, name='delete_chit_details'),
]