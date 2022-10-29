import pytest
from django.urls import reverse

from consulta_expediente.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('expedientes:clientes'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Expedientes</title>')
