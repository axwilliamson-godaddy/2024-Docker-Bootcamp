from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^sleep$', views.i_take_so_long_to_load, name='sleep'),
    url(r'^sleep/(?P<how_long>[0-9]+)$', views.i_take_so_long_to_load, name='sleep'),
    url(r'^error$', views.raise_error, name='error'),

]
