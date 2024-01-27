from django.urls import path 
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('elements/', Elements, name='elements'),
    path('job_detail/', Job_Detail, name='job_detail'),
    path('job_listing/', Job_Listing, name='job_listing'),
    path('main/', Main, name='main'),
    path('single_blog/', Single_Blog, name='single_blog'),
]
