import pytest
import requests
from pytest_bdd import given, parsers

@pytest.fixture
def context():
    return {
        'ids_para_limpeza': []
    }

@pytest.fixture(autouse=True)
def gerenciador_de_limpeza(context):
    yield 
    
    base_url = context.get('base_url')
    endpoint = context.get('endpoint')
    ids = context.get('ids_para_limpeza', [])

    if base_url and endpoint and ids:
        for comentario_id in ids:
            url_delete = f"{base_url}{endpoint}/{comentario_id}"
            try:
                print(f"Limpando comentario de ID {comentario_id}...")
                requests.delete(url_delete)
            except Exception as e:
                print(f"Erro ao tentar limpar cometario de ID {comentario_id}: {e}")

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

    context['ids_para_limpeza'].append(context['id_comentario_criado'])