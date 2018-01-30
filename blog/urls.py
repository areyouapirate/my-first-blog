from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^inscriptions/$', views.inscr_list, name='inscr_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail, name='user_detail'),
	url(r'^your_profile/$', views.profile_detail, name='profile_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^inscr/new/$', views.inscr_new, name='inscr_new'),
	url(r'^inscr/(?P<pk>[0-9]+)/$', views.inscr_detail, name='inscr_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^admin/', admin.site.urls),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
	url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	url(r'^post_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<pidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
	        views.post_confirm, name='post_confirm'),
	url(r'^place/new/$', views.place_new, name='place_new'),
	url(r'^places/$', views.place_list, name='place_list'),
	url(r'^place/(?P<pk>[0-9]+)/$', views.place_detail, name='place_detail'),
]