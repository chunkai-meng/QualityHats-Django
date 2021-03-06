from django.conf.urls import url
from . import views

app_name = 'order_app'
urlpatterns = [
    url(r'^$', views.OrderListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='detail'),
    url(r'^create/$', views.OrderCreateView.as_view(), name='create'),
    url(r'update/(?P<pk>\d+)/$', views.OrderUpdateView.as_view(), name='update'),
    url(r'delete/(?P<pk>\d+)/$', views.OrderDeleteView.as_view(), name='delete'),
]
