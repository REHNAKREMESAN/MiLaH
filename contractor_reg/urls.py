from django.conf.urls import url
from .views import contractor_reg

app_name = 'contractor_reg'


urlpatterns = [
    url(r'^$', contractor_reg, name='ContractorForms')
]


