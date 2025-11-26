import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/local.feature', 'Criar um novo Local com sucesso')
def test_run():
    pass

@when(parsers.parse('envio um novo local com nome "{nome}", endereco "{endereco}", categoria "{categoria}", latitude "{latitude}", longitude "{longitude}"'))
def send_post_local_success(context, nome, endereco, categoria, latitude, longitude):
    """
    Envia a requisição POST para o endpoint /local com os dados capturados do Gherkin.
    """
    full_url = context['full_url']
    
    payload = {
        "nome": nome,
        "endereco": endereco,
        "categoria": categoria,
        "latitude": latitude,
        "longitude": longitude
    }
    
    response = requests.post(full_url, json=payload)
    context['response'] = response
    
    if response.status_code == 201:
        created_data = response.json()
        context['id_local_criado'] = created_data.get('local_id')
        context['created_local_name'] = nome

        novo_id = context['response'].json().get('local_id')
        context['ids_para_limpeza'].append(novo_id)
    

@then(parsers.parse('o campo "local_id" deve ser preenchido (não nulo)'))
def check_local_id_is_not_null(context):
    """Verifica se o ID do Local foi criado e retornado pela API."""
    json_data = context['response'].json()
    local_id = json_data.get('local_id')
    
    assert local_id is not None
    assert isinstance(local_id, int) or isinstance(local_id, str), "O campo 'local_id' deve ser um número ou string."