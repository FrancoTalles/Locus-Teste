import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers



# --- CENÁRIO - (GET) ---

@scenario('features/local.feature', 'Listar todos os Locais Cadastrados')
def test_listar_locais():
    """Define e executa o cenário de listagem de locais."""
    pass


@when(parsers.parse('envio uma requisição GET para /local'))
def send_get_all_request(context):
    try:
        context['response'] = requests.get(context['full_url'])
    except requests.exceptions.ConnectionError as e:
        pytest.fail(f"Falha ao conectar à api em {context['full_url']}: {e}")


@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):

    assert context['response'].status_code == 200

@then(parsers.parse('deve retornar uma lista de locais'))
def check_response_is_list(context):
    
    try:
        json_data = context['response'].json()
        assert isinstance(json_data, list)
        #lista não está vazia
        assert len(json_data) > 0, "A lista de locais retornada está vazia."
    except requests.exceptions.JSONDecodeError:
        pytest.fail("O corpo da resposta não é um JSON válido.")

@then(parsers.parse('cada local deve conter os campos "{campos_string}"'))
def check_local_schema(context, campos_string):
    
    json_data = context['response'].json()
    
    # Processa os campos esperados (separados por vírgula e removendo aspas)
    campos_esperados = {campo.strip().replace('"', '') for campo in campos_string.split(',')}
    
    for i, local in enumerate(json_data):
        chaves_recebidas = set(local.keys())
        
        
        missing_fields = campos_esperados.difference(chaves_recebidas)
        
        assert not missing_fields, (
            f"Local no índice {i} ({local.get('local_id', 'ID desconhecido')}) está faltando os campos: {missing_fields}"
        )
        