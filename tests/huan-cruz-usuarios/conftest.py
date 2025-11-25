import pytest
import requests
import time
from pytest_bdd import given, parsers

@pytest.fixture
def context():
    return {}

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de usuarios é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint

@given('que tenho usuários cadastrados no sistema')
def create_user_for_setup(context):
    full_url = f"{context['base_url']}{context['endpoint']}"

    email_unique = f"setup_{int(time.time()*1000)}@example.com"

    payload = {
        "nome": "Usuario Setup",
        "email": email_unique,
        "senha_hash": "123456",
        "foto_perfil": ""
    }

    r = requests.post(full_url, json=payload)

    assert r.status_code in (200, 201), f"Falha ao criar usuário de setup: {r.text}"

    result = r.json()
    user_id = result.get("id") or result.get("usuario_id")

    assert user_id is not None, "Resposta não contém ID de usuário"

    context["id_usuario"] = user_id
