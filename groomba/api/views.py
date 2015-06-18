import pytz
import iso8601
from datetime import datetime
from django.views.generic import View
from django.http import JsonResponse

from groomba.gcalendar.tasks import get_available_rooms


class AvailableRoomsView(View):
    """Records the current user's interest in an author."""

    def get(self, request, *args, **kwargs):

        start_string = kwargs.get('start')
        end_string = kwargs.get('end')
        start = iso8601.parse_date(start_string)
        end = iso8601.parse_date(end_string)
        rooms = get_available_rooms(start, end)
        data = {'rooms': rooms}
        return JsonResponse(data)
