`GET /events` - get all events

`POST /event` - create event

```json
{
    "start_time": "2024-01-27T12:00:00",
    "end_time": "2024-01-27T13:00:00",
    "place": "Gym",
    "color": "red",
    "minutes_before_event": 30,
    "attendee_id": 1,
    "creator_id": 2,
    "event_type": "trening"
}
```

`POST /ingredients` - add ingredients

```json
[
    {
        "name": "Tomato",
        "calories": 22
    },
    {
        "name": "Cucumber",
        "calories": 16
    }
]
```