from django.conf.urls import url
from forum import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tag/(?P<tag>[\w_-]+)/$', views.index, name="index_tagged"),

]
