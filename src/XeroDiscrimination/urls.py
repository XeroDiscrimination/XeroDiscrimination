"""XeroDiscrimination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from jobs import views
from accounts import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('',v.recommend_detail,name='index'),
    path('rainbow_tick/',views.rainbow_tick,name='rainbow_tick'),
    path('jobs/',include('jobs.url')),
    path('profile/',views.profile, name='profile'),
    path('organisation/',views.organisation, name='organisation'),
    path('rainbow_tick/job-single.html',views.job_single, name='job_single'),
    # path('rainbow_tick/blog.html',views.job_single, name='job_single'),
    
    path('test',views.test, name='test'),
    path('test1',views.test1, name='test1'),
    # path('company_details', v.company_detail, name='company_detail')
    path('company_details/', include('accounts.url') ),
    path('promote_organization', v.recommend_detail, name='recommend_organization')
] 
