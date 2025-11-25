import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers

# ID que será usado para a busca bem-sucedida
EXISTING_ID = 1 
EXISTING_LOCAL_NAME = "Largo Sao Sebastiao" 


@pytest.fixture
def context():
    """Fixture para compartilhar dados (estado) entre os steps de um cenário."""
    return {
        'base_url': "http://localhost:3000",
        'endpoint': "/local",
        'full_url': "http://localhost:3000/local", 
        'response': None
    }


@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    assert context['base_url'] == url

@given(parsers.parse('que o endpoint de local é "{endpoint}"'))
def set_endpoint(context, endpoint):
    assert context['endpoint'] == endpoint
    expected_full_url = f"{context['base_url']}{context['endpoint']}"
    assert context['full_url'] == expected_full_url

# --- CENÁRIO (GET por ID) ---

@scenario('features/local.feature', 'Listar um Local ao buscar por ID')
def test_buscar_local_por_id_existente():
    """Define e executa o cenário de busca por ID existente."""
    pass


@given('que tenho locais cadastrados no sistema')
def setup_locais_cadastrados_for_find(context):
    """
    Garante que o Local com ID 1 existe para o teste.
    Em um ambiente real, você faria um POST aqui, mas para simulação,
    apenas definimos o ID esperado e o Nome esperado.
    """
    context['local_id_to_find'] = EXISTING_ID
    context['expected_name'] = EXISTING_LOCAL_NAME
    pass



@when(parsers.parse('pesquiso pelo local com ID {local_id:d}'))
def send_get_by_id_request(context, local_id):
    """Envia a requisição GET para /local/{id}."""
    context['local_id'] = local_id 
    url_with_id = f"{context['full_url']}/{local_id}"
    try:
        context['response'] = requests.get(url_with_id)
    except requests.exceptions.ConnectionError as e:
        pytest.fail(f"Falha ao conectar à API em {url_with_id}: {e}")


@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "local_id" deve ser igual a {expected_id:d}'))
def check_id_match(context, expected_id):
    """Verifica se o ID retornado no corpo do JSON é o ID esperado (1)."""
    json_data = context['response'].json()
    assert json_data.get('local_id') == expected_id, (
        f"Esperado local_id: {expected_id}, Recebido: {json_data.get('local_id')}"
    )

@then(parsers.parse('o campo "nome" do local deve ser "{expected_name}"'))
def check_local_name(context, expected_name):
    """Verifica se o nome do local retornado é o nome esperado."""
    json_data = context['response'].json()
    assert json_data.get('nome') == expected_name, (
        f"Esperado nome: {expected_name}, Recebido: {json_data.get('nome')}"
    )