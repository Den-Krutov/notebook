from fastapi.testclient import TestClient

from .. import create_app

client = TestClient(
    app=create_app(),
    base_url='http://test/api/v1/organizations'
)


def test_write_or_overwrite_organization_response_with_valid_data():
    response = client.post('/write_data', json={
        'phone': '88005553535', 'address': 'test1'})
    assert response.status_code == 200
    expected_response = {
        'phone': '88005553535',
        'address': 'test1'
    }
    assert response.json() == expected_response
    response = client.post('/write_data', json={
        'phone': '88005553535', 'address': 'test2'})
    assert response.status_code == 200
    expected_response = {
        'phone': '88005553535',
        'address': 'test2'
    }
    assert response.json() == expected_response


def test_check_organization_response_with_valid_data():
    response = client.get('/check_data', params={'phone': '88005553535'})
    assert response.status_code == 200
    expected_response = {
        'phone': '88005553535',
        'address': 'test2'
    }
    assert response.json() == expected_response


def test_check_organization_response_with_not_valid_data():
    response = client.get('/check_data', params={'phone': '8800'})
    assert response.status_code == 404
    expected_response = {
        "detail": "Несуществующий номер телефона",
    }
    assert response.json() == expected_response


def test_check_organization_response_with_not_found_data():
    response = client.get('/check_data', params={'phone': '88005553540'})
    assert response.status_code == 404
    expected_response = {
        "detail": "Нет организации с таким номером",
    }
    assert response.json() == expected_response


def test_write_or_overwrite_organization_response_with_not_valid_data():
    response = client.post('/write_data', json={
        'phone': '8800', 'address': 'test'})
    assert response.status_code == 422
