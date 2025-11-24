import pytest
import requests
from pytest_bdd import given, parsers

@pytest.fixture
def context():
    return {}

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de posts é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint

@given(parsers.parse('que tenho posts cadastrados no sistema'))
def ensure_posts_exist(context):
    full_url = f"{context['base_url']}{context['endpoint']}"
    
    novo_post = {
        "descricao": "Post Criado Automaticamente pelo Setup",
        "usuario_id": 2,
        "local_id": 1,
        "imagem": ""
    }
    
    response = requests.post(full_url, json=novo_post)
    
    assert response.status_code == 201, "Falha ao criar post de setup"
    
    context['id_post_criado'] = response.json().get('post_id')