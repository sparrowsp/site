from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.emage_list, name='emage_list'),
    #url(r'^$', views.ImageListView.as_view(), name='image_list'),


    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]
