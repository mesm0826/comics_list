from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'comics_list_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', auth_views.login, {'template_name': 'comics_list_app/login.html'}, name='login'),
    url(r'^add$', views.edit, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]
