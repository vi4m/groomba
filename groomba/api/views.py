import pytz
import iso8601
from datetime import datetime
from django.views.generic import View
from django.http import JsonResponse

from groomba.gcalendar.tasks import get_available_rooms, create_event


class AvailableRoomsView(View):

    def get(self, request, *args, **kwargs):
        start_string = kwargs.get('start')
        end_string = kwargs.get('end')
        start = iso8601.parse_date(start_string)
        end = iso8601.parse_date(end_string)
        rooms = get_available_rooms(start, end)
        data = {'rooms': rooms}
        return JsonResponse(data)


class CreateEventView(View):

    def post(self, request, *args, **kwargs):
        start_string = self.request.POST.get('start')
        end_string = self.request.POST.get('end')
        room_id = self.request.POST.get('room_id')
        summary = self.request.POST.get('summary')
        description = self.request.POST.get('description')
        start = iso8601.parse_date(start_string)
        end = iso8601.parse_date(end_string)

        event = create_event(
            start, end, room_id, summary, description
        )
        return JsonResponse(event)
