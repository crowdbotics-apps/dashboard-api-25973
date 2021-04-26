import json
from typing import Callable

import pytest
from django.conf import settings
from rest_framework.test import APIRequestFactory, force_authenticate

from dashboard.api.tests.factories import AppFactory
from dashboard.api.v1.viewsets import AppViewSet
from users.tests.factories import UserFactory


pytestmark = pytest.mark.django_db


@pytest.fixture
def request_factory():
    return APIRequestFactory()


@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def app_view():
    return AppViewSet.as_view({"post": "create", "get": "list"})


def test_post_app(
        user: settings.AUTH_USER_MODEL,
        request_factory: APIRequestFactory,
        app_view: Callable
):
    app_payload = {
        "name": "awesome",
        "description": "Very good",
        "type": "Web",
        "framework": "Django"
    }
    request = request_factory.post(
        '/api/v1/apps/',
        app_payload
    )
    force_authenticate(request, user=user)
    response = app_view(request)
    assert response.status_code == 201
    assert response.data["name"] == app_payload["name"]


def test_list_apps(
        user: settings.AUTH_USER_MODEL,
        request_factory: APIRequestFactory,
        app_view: Callable
):
    app = AppFactory.create(user=user)
    request = request_factory.get('/api/v1/apps/')
    force_authenticate(request, user=user)
    response = app_view(request)
    assert response.data[0]["name"] == app.name
    assert response.data[0]["description"] == app.description
    assert len(response.data) == 1
