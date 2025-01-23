import pytest
from rest_framework import status
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def task():
    return Task.objects.create(title='Test Task', description='Test Description')
@pytest.mark.django_db
def test_create_task(client):
    url = '/api/tasks/'
    data = {'title': 'New Task', 'description': 'New Description'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == data['title']
@pytest.mark.django_db
def test_get_tasks(client, task):
    url = '/api/tasks/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
@pytest.mark.django_db
def test_update_task(client, task):
    url = f'/api/tasks/{task.id}/'
    data = {'title': 'Updated Task', 'description': 'Updated Description'}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == data['title']
@pytest.mark.django_db
def test_delete_task(client, task):
    url = f'/api/tasks/{task.id}/'
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()
