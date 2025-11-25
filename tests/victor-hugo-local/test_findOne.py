import pytest
import requests
from pytest_bdd import scenario,  when, then, parsers


# --- CENÁRIO (GET por ID) ---

@scenario('features/local.feature', 'Listar um Local ao buscar por ID')
def test_buscar_local_por_id_existente():
    """Define e executa o cenário de busca por ID existente."""
    pass


@when(parsers.parse('pesquiso pelo local com ID {local_id:d}'))
def send_get_by_id_request(context, local_id):
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