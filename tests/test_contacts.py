import pytest
from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate

from contacts.models import Contact
from contacts.serializers import ContactSerializer, FullContactSerializer

api_client = APIClient()


def test_with_no_authenticated_client(client, django_user_model):
    response = client.get('/')
    assert response.status_code == 200


def test_with_authenticated_client(admin_client, django_user_model):
    response = admin_client.get('/contact-list')
    assert response.status_code == 301


@pytest.mark.django_db
def test_list_of_contacts(admin_client):
    url = reverse('contact_list')
    response = admin_client.get(url)

    assert response.status_code == 200
    assert response.data["contacts"] is not None


@pytest.mark.django_db
def test_create_contact_1():
    category = Contact.objects.create(
        name="John",
        email="john@media.com",
        subject="App support",
        message="Testing John",
        status="New"
    )
    assert category.status == "New"


@pytest.mark.django_db
def test_create_contact_2(admin_client):
    url = "/contact/"

    payload = {
        "name": "Terry Johns",
        "email": "terry@media.com",
        "subject": "Other",
        "message": "Testing Terry",
        "status": "Resolved"
    }
    response = admin_client.post(url, payload)
    print(response)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_contacts(admin_client, create_contact):
    response = admin_client.get(reverse('contact_list'))
    assert response.status_code == status.HTTP_200_OK
