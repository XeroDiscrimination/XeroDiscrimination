from django.conf.urls import url
from accounts.views import company_detail, companyListView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('<slug:slug>', company_detail, name='company_detail'),
    path('', companyListView.as_view(), name='company_list'),
]