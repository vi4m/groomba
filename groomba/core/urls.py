from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from groomba.core.views import HomePageView

urlpatterns = patterns(
    '',
    url(
        r'^start/', HomePageView.as_view(), name='homepage',
    ),
)
