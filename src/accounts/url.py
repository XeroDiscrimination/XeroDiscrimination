from django.conf.urls import url
from accounts.views import company_detail
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('<slug:slug>', company_detail, name='company_detail'),
    # path('', ArticleListView.as_view(), name='article_list'),
]