# accounts/urls.py
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/',views.SignUp.as_view(), name='signup'),
]
