import pytz
import iso8601
import json
from datetime import datetime
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateEventView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        start_string = data.get('start')
        end_string = data.get('end')
        room_id = data.get('room_id')
        summary = data.get('summary')
        description = data.get('description')
        start = iso8601.parse_date(start_string)
        end = iso8601.parse_date(end_string)

        event = create_event(
            start, end, room_id, summary, description
        )
        return JsonResponse(event)
