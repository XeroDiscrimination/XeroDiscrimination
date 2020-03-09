from django.conf.urls import url
from jobs import views
from django.urls import path

app_name = 'jobs'

urlpatterns = [
    path('search-result/',views.search_result,name='search_result'),
    path('blog/',views.blog,name='blog'),
    path('new_post/',views.new_post,name='new_post'),
    path('job_post/',views.job_post,name='job_post'),
    path('job_single/',views.job_single,name='job_single'),
    path('test/',views.test, name='test'),
    path('test1/',views.test1, name='test1'),

]
