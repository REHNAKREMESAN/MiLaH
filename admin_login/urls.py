from django.conf.urls import url
from .views import login, adminhome


app_name = 'admin_login'
urlpatterns = [
    url(r'^$', login, name='AdminLoginForms'),
    url(r'^adminhome', adminhome, name='adminhome')
]