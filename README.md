# Events

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

# Ingredients

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

# Meals

`GET /meals` - get all meals
```json
[
    {
        "calories": 500,
        "id": 1
    }
]
```

`POST /meals` - add meal

```json
{
    "name": "Chicken Salad",
    "calories": 350,
    "ingredients": [
        {
            "name": "Chicken",
            "calories": 200
        },
        {
            "name": "Lettuce",
            "calories": 10
        },
        {
            "name": "Tomatoes",
            "calories": 20
        },
        {
            "name": "Cucumbers",
            "calories": 15
        },
        {
            "name": "Salad Dressing",
            "calories": 105
        }
    ]
}
```