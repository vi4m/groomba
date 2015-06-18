from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from groomba.api.views import AvailableRoomsView, CreateEventView


urlpatterns = patterns(
    '',
    url(
        r'^available-rooms/(?P<start>[^\/].*)/(?P<end>[^\/].*)/$',
        login_required(AvailableRoomsView.as_view()),
        name='available-rooms',
    ),
    url(
        r'^create-event/$',
        CreateEventView.as_view(),
        name='create-event',
    )
)
