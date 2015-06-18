from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from groomba.api.views import AvailableRoomsView


urlpatterns = patterns(
    '',
    url(
        r'^available-rooms/(?P<start>[^\/].*)/(?P<end>[^\/].*)/$',
        login_required(AvailableRoomsView.as_view()),
        name='available-rooms',
    ),
)
