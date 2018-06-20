from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.friend_list, name='friend_list'),
  #  url(r'^addr/friend/(?P<pk>\d+)/$', views.friend_detail, name='friend_detail'),
    #url(r'^blog/post/new/$', views.post_new, name='post_new'),
    #url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]