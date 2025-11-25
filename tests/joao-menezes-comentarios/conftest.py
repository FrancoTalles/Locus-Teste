import pytest
import requests
from pytest_bdd import given, parsers

@pytest.fixture
def context():
    return {}

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de comentarios é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint

@given(parsers.parse('que tenho comentarios cadastrados no sistema'))
def ensure_comentarios_exist(context):
    full_url = f"{context['base_url']}{context['endpoint']}"
    
    novo_comentario = {
        "comentario": "Comentario criado",
        "usuario_id": 4,
        "post_id": 2,
    }
    
    response = requests.post(full_url, json=novo_comentario)
    
    assert response.status_code == 201, "Falha ao criar comentario"
    
    context['id_comentario_criado'] = response.json().get('comentario_id')