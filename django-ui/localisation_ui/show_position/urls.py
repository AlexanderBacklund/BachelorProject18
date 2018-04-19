from django.conf.urls import url
from show_position import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
]
