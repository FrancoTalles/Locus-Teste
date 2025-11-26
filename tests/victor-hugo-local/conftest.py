import pytest
import requests
from pytest_bdd import given, parsers, then

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
        for local_id in ids:
            url_delete = f"{base_url}{endpoint}/{local_id}"
            try:
                print(f"Limpando local de ID {local_id}...")
                requests.delete(url_delete)
            except Exception as e:
                print(f"Erro ao tentar limpar local de ID {local_id}: {e}")

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de local é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint

    context['full_url'] = f"{context['base_url']}{context['endpoint']}"

@given(parsers.parse('que tenho locais cadastrados no sistema'))
def ensure_locais_exist(context):
    full_url = f"{context['base_url']}{context['endpoint']}"
    
    novo_local = {
        "nome": "Local criado",
        "endereco": "Rua Teste, 100",
        "categoria": "Temporario",
        "latitude": "-1.0",
        "longitude": "-1.0"
    }

    response = requests.post(full_url, json=novo_local)
    print(response.json())
    assert response.status_code == 201, "Falha ao criar local de setup"
    
    context['id_local_criado'] = response.json().get('local_id')

    context['ids_para_limpeza'].append(context['id_local_criado'])

    context['created_local_name'] = response.json().get('nome')

@then(parsers.parse('o sistema deve retornar status "{status_str}"'))
def check_status_code(context, status_str):
    """
    Verifica se o status code da resposta corresponde ao esperado,
    lendo o status como uma string do Gherkin.
    """
    try:
        expected_status = int(status_str)
    except ValueError:
        pytest.fail(f"O valor de status '{status_str}' no Gherkin não é um número válido.")
        
    assert context['response'].status_code == expected_status

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field_str_value(context, campo, valor):
    """
    Step genérico que compara o valor de um campo JSON com um valor string/numérico
    capturado do Gherkin (usado para validar 'nome', 'categoria', etc.).
    """
    json_data = context['response'].json()
    
    assert str(json_data.get(campo)) == str(valor), (
        f"Erro no campo '{campo}': Esperado '{valor}', Recebido '{json_data.get(campo)}'"
    )