from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.image_list, name='image_list'),
    #url(r'^$', views.ImageListView.as_view(), name='image_list'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<image>[-\w]+)/$',
        views.image_detail,
        name='image_detail'),
    #url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]
