import pytest
from fastapi.testclient import TestClient
from main import app  # replace with the name of your FastAPI app

client = TestClient(app)


def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_event():
    event_data = {
        "start_time": "2024-01-27T12:00:00",
        "end_time": "2024-01-27T13:00:00",
        "place": "Gym",
        "color": "red",
        "minutes_before_event": 30,
        "attendee_id": 1,
        "creator_id": 2,
        "event_type": "trening"
    }
    response = client.post("/event", json=event_data)
    assert response.status_code == 200
    response_data = response.json()
    for key in event_data:
        if key in ["start_time", "end_time"]:
            assert event_data[key][:10] == response_data[key]  # compare only the date part
        else:
            assert event_data[key] == response_data[key]


def test_get_ingredients():
    response = client.get("/ingredients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_ingredients():
    ingredients_data = [
        {
            "name": "Tomato",
            "calories": 22
        },
        {
            "name": "Cucumber",
            "calories": 16
        }
    ]
    response = client.post("/ingredients", json=ingredients_data)
    assert response.status_code == 200
    response_data = response.json()
    for i in range(len(ingredients_data)):
        for key in ingredients_data[i]:
            assert ingredients_data[i][key] == response_data[i][key]


def test_get_meals():
    response = client.get("/meals")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_meals():
    meal_data = {
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
    response = client.post("/meals", json=meal_data)
    assert response.status_code == 200
    response_data = response.json()
    for key in meal_data:
        if key == "ingredients":
            for i in range(len(meal_data[key])):
                for sub_key in meal_data[key][i]:
                    assert meal_data[key][i][sub_key] == response_data[key][i][sub_key]
        else:
            assert meal_data[key] == response_data[key]


def test_get_reports():
    response = client.get("/reports")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_report():
    report_data = {
        "first_name": "John",
        "last_name": "Doe",
        "description": "This is a sample report for testing purposes.",
        "result": "sprained ankle"
    }
    response = client.post("/report", json=report_data)
    assert response.status_code == 200
    response_data = response.json()
    for key in report_data:
        assert report_data[key] == response_data[key]


def test_get_plans_meals():
    response = client.get("/plans_meals")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_plans_meals():
    plans_meals_data = {
        "meal_id": 3
    }
    response = client.post("/plans_meals", json=plans_meals_data)
    assert response.status_code == 200
    response_data = response.json()
    for key in plans_meals_data:
        assert plans_meals_data[key] == response_data[key]
