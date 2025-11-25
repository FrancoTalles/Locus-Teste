import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers


@pytest.fixture
def context():
    """Fixture para compartilhar dados entre os steps."""
    return {
        'base_url': "http://localhost:3000",
        'endpoint': "/local",
        'full_url': "http://localhost:3000/local",
        'response': None
    }


@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    """Verifica se a URL base na fixture corresponde à do Gherkin."""
    assert context['base_url'] == url
    # Este step garante que o Pytest BDD encontre o step do Background.

@given(parsers.parse('que o endpoint de local é "{endpoint}"'))
def set_endpoint(context, endpoint):
    """Verifica o endpoint e confirma a URL completa."""
    assert context['endpoint'] == endpoint
    expected_full_url = f"{context['base_url']}{context['endpoint']}"
    assert context['full_url'] == expected_full_url


# --- CENÁRIO - (GET) ---

@scenario('features/local.feature', 'Listar todos os Locais Cadastrados')
def test_listar_locais():
    """Define e executa o cenário de listagem de locais."""
    pass

@given('que tenho locais cadastrados no sistema')
def setup_locais_cadastrados(context):
    """
    Garante que a API tenha dados para retornar.
    Em um teste real, você forçaria a criação de dados aqui.
    Para simulação: assume-se que o endpoint já tem dados.
    """
    # Apenas verifica se a URL está configurada
    assert 'full_url' in context
    pass


@when(parsers.parse('envio uma requisição GET para /local'))
def send_get_all_request(context):
    """Envia a requisição GET para o endpoint de listagem."""
    try:
        context['response'] = requests.get(context['full_url'])
    except requests.exceptions.ConnectionError as e:
        pytest.fail(f"Falha ao conectar à api em {context['full_url']}: {e}")


@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):
    """Verifica se o status da resposta é 200."""
    assert context['response'].status_code == 200

@then(parsers.parse('deve retornar uma lista de locais'))
def check_response_is_list(context):
    """Verifica se o corpo da resposta é uma lista (JSON array)."""
    try:
        json_data = context['response'].json()
        assert isinstance(json_data, list)
        #lista não está vazia
        assert len(json_data) > 0, "A lista de locais retornada está vazia."
    except requests.exceptions.JSONDecodeError:
        pytest.fail("O corpo da resposta não é um JSON válido.")

@then(parsers.parse('cada local deve conter os campos "{campos_string}"'))
def check_local_schema(context, campos_string):
    """Verifica se todos os locais na lista contêm os campos esperados."""
    json_data = context['response'].json()
    
    # Processa os campos esperados (separados por vírgula e removendo aspas)
    campos_esperados = {campo.strip().replace('"', '') for campo in campos_string.split(',')}
    
    for i, local in enumerate(json_data):
        chaves_recebidas = set(local.keys())
        
        
        missing_fields = campos_esperados.difference(chaves_recebidas)
        
        assert not missing_fields, (
            f"Local no índice {i} ({local.get('local_id', 'ID desconhecido')}) está faltando os campos: {missing_fields}"
        )
        