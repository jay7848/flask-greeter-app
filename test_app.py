from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Flask Greeter App!' in response.data

def test_greet():
    client = app.test_client()
    response = client.post('/greet', data={'name': 'Alice'})
    assert response.status_code == 200
    assert b'Hello, Alice!' in response.data
