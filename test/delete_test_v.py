import requests


def test_add():
    body = {"title": "new work", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['completed'] is None
    id = response.json()["id"]
    requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 200
