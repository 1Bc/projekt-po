`GET /events` - get all events

`POST /event` - create event

```json
{
    "start_time": "2023-05-01T12:00:00",
    "end_time": "2023-05-01T16:00:00",
    "place": "Gym",
    "color": "red",
    "minutes_before_event": 30,
    "attendee_id": 1,
    "creator_id": 2,
    "event_type": "trening"
}
```