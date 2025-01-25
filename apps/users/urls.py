from apps.users.views import log_in, sign_up, log_out
from django.urls import path

urlpatterns = [
    path('log in', log_in, name='log in'),
    path('sign up', sign_up, name='sign up'),
    path('log out', log_out, name='log out')
]