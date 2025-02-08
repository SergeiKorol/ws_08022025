import requests


def test_add():
    body = {"title": "ssss", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]

    body = {"completed": True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()["completed"] is True