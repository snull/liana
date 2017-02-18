from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'^posts/list/$', views.list, name="list"),
    url(r'^api/posts/new/$', views.new_post, name="new_post"),
    url(r'^api/posts/list/$', views.list_json, name="list_json"),
    url(r'^register/$', views.register, name="register"),
    url(r'^posts/create/$', views.create_post, name="create_post"),
    url(r'^posts/edit/(?P<id>[0-9]+)$', views.edit_post, name="edit_post"),
]
