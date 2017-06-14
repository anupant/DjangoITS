__author__ = 'Anna'
from django.conf.urls import url
from . import views
app_name = 'photos'

urlpatterns = [ #url(r'^$',views.index,name ='index'),
                url(r'^$',views.IndexView.as_view(),name ='index'),

                 #Register
                 url(r'register/$',views.UserFormView.as_view(),name ='register'),

                # /music/<album_id>/
                #url(r'^(?P<album_id>[0-9]+)/$',views.detail,name = 'detail'),
                url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name = 'detail'),
                # /music/<album_id>/favorite
                #url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name = 'favorite'),

                #/photos/album/add/
                url(r'album/add/$',views.AlbumCreate.as_view(),name ='album-add'),

                #/photos/album/2/
                url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name ='album-update'),

                #/photos/album/2/delete/
                url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name ='album-delete'),


                ]