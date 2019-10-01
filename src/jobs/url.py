from django.conf.urls import url
from django.conf.urls import path
from jobs import views

urlpatterns = [
    url(r'^about$',views.AboutView.as_view(),name='about')
]