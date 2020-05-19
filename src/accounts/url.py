from django.conf.urls import url
from accounts.views import company_detail, companyListView, recommend_detail, ywca_admin,company_update
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('company/<slug:slug>', company_detail, name='company_detail'),
    path('', companyListView.as_view(), name='company_list'),
    path('ywcaadmin',ywca_admin.as_view(), name='ywcaAdmin'),
    path('company/<slug:slug>/edit', company_update, name='company_update'),
]