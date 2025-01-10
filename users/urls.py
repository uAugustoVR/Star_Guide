from users.views import log_in, sign_up
from django.urls import path

urlpatterns = [
    path('log in', log_in, name='log in'),
    path('sign up', sign_up, name='sign up')
]