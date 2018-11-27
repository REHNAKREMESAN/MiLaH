from .views import add_status
from django.conf.urls import url

app_name = 'add_status'
urlpatterns = [
    url(r'^chit_memb/(?P<pk>\d+)$', chit_draw_memb, name='chit_draw_memb')
]