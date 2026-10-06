from django.urls import path
from .views import Hello, People, hello_api, people_api

urlpatterns = [
    path('hello/', Hello.as_view(), name='hello-message'),
    path('func/', hello_api, name='hello-func'), 
    path('people/', People.as_view(), name='people-info'),
    path('people/func/', people_api, name='people-info-func'),
] 