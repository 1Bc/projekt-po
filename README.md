# Events

`GET /events` - get all events
```json
[
    {
        "id": 2,
        "minutes_before_event": 30,
        "creator_id": 2,
        "report_id": null,
        "meals_plan_id": null,
        "start_time": "2023-05-01",
        "end_time": "2023-05-01",
        "place": "Gym",
        "color": "red",
        "attendee_id": 1,
        "event_type": "trening",
        "comment_id": null
    }
]
```

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
`GET /ingredients` - get ingredients
```json
[
    {
        "calories": 200,
        "id": 21,
        "name": "Chicken"
    },
    {
        "calories": 10,
        "id": 22,
        "name": "Lettuce"
    }
]
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

# Reports

`GET /reports` - get all reports
```json
[
    {
        "last_name": "Doe",
        "result": "Success",
        "first_name": "John",
        "description": "This is a sample report for testing purposes.",
        "id": 1
    }
]
```

`POST /report` - add report
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "description": "This is a sample report for testing purposes.",
    "result": "sprained ankle"
}
```

# Meal Plans
`GET /plans_meals` - get all meal plans
```json
[
    {
        "meal_id": 2,
        "plan_id": null
    },
    {
        "meal_id": 3,
        "plan_id": null
    }
]
```

`POST /plans_meals` - add meal plans
```json
{
    "meal_id": 3,
    "plan_id": 2
}
```

# Comment
`GET /comments` - get all comments
```json
[
    {
        "event_id": 1,
        "id": 1,
        "description": "This is a comment."
    }
]
```

`POST /comment` - add comment
```json
{
    "event_id": 1,
    "description": "This is a comment."
}
```