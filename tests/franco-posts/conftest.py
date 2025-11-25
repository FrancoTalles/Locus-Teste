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
        for post_id in ids:
            url_delete = f"{base_url}{endpoint}/{post_id}"
            try:
                print(f"Limpando post de ID {post_id}...")
                requests.delete(url_delete)
            except Exception as e:
                print(f"Erro ao tentar limpar post de ID {post_id}: {e}")

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

    context['ids_para_limpeza'].append(context['id_post_criado'])