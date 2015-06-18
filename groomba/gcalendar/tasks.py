from django.core.cache import caches
from apiclient.errors import HttpError

from groomba.gcalendar.auth import get_service


def get_available_rooms(start, end):
    service = get_service()
    calendars = get_calendars()
    calendars_dict = {}
    for calendar in calendars:
        calendars_dict[calendar['id']] = calendar['summary']
    body = {
        'timeMin': start.isoformat(),
        'timeMax': end.isoformat(),
        'timezone': 'CEST',
        'items': calendars
    }
    try:
        result = service.freebusy().query(body=body).execute()
    except HttpError as err:
        print(err.content)

    status_calendars = result.get('calendars')
    available_rooms = []
    for name, value in status_calendars.items():
        if not value.get('busy'):
            available_rooms.append({
                'name': calendars_dict.get(name),
                'id': name,
            })
    return available_rooms


def get_calendars():
    cache = caches['default']
    cache.set('my_key', 'hello, world!', 30)
    calendars = cache.get('calendars')
    if not calendars:
        service = get_service()
        items = service.calendarList().list().execute()
        calendars = [{'id': calendar['id'], 'summary': calendar['summary']} for calendar in items['items']]
        cache.set('calendars', calendars, 3600)
    return calendars
