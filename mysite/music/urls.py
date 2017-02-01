from django.conf.urls import url

from . import views
from django.contrib.auth.decorators import login_required


app_name='music'
login_url="/music/login_user/"

urlpatterns = [
	# /music/
    #url(r'^$', views.IndexView, name='index'),
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    # /music/login_user
    url(r'^login_user/$', views.login_user, name='login_user'),
    # /music/logout_user
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # /music/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /music/71
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/songs/
    url(r'^song/$', views.SongView.as_view(), name='song'),
    # /music/album/add
    #url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/add/$', views.AlbumCreate, name='album-add'),
    # /music/71/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/71/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    # /music/album/71/add
    url(r'^album/(?P<pk>[0-9]+)/add/$', views.SongCreate.as_view(), name='song-add'),
    # /music/3/delete_song/1
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # /music/3/favourite_song
    url(r'^(?P<song_id>[0-9]+)/favourite_song/$', views.favourite_song, name='favourite_song'),
    # /music/3/favourite_album
    url(r'^(?P<album_id>[0-9]+)/favourite_album/$', views.favourite_album, name='favourite_album'),
    url(r'^restricted/$', views.restricted, name='restricted' ),

]