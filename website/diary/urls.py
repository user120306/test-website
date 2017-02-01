from django.conf.urls import url

from . import views

app_name='diary'

urlpatterns = [
	# /diary
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /diary/post/add
    url(r'^post/add/$', views.PostCreate.as_view(), name='post-add'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),    
    url(r'^post/(?P<pk>[0-9]+)/edit$', views.PostUpdate.as_view(), name='post-update'),
    url(r'^post/(?P<pk>[0-9]+)/add/$', views.EntryCreate.as_view(), name='entry-add'),
    url(r'^post/(?P<pk>[0-9]+)/entry/add/$', views.EntryUpdate.as_view(), name='entry-update'),
	url(r'^post/(?P<post_id>[0-9]+)/entry/(?P<entry_id>[0-9]+)/delete/$', views.delete_entry, name='entry-delete'),
 	]