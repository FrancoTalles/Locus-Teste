import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/local.feature', 'Atualizar um Local existente com sucesso')
def test_run():
    pass

@when(parsers.parse('atualizo o local criado anteriormente com a nova categoria "{nova_categoria}"'))
def update_dynamic_post(context, nova_categoria):
    local_id = context['id_local_criado']
    
    full_url = f"{context['base_url']}{context['endpoint']}/{local_id}"
    
    payload = {
        "categoria": nova_categoria,
    }
    
    context['response'] = requests.patch(full_url, json=payload)
    print(context['response'].json())

@then('o sistema deve retornar status 200')
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "{nome}" deve permanecer o original'))
def check_field_str_original(context):
    expected_name = context['created_local_name'] 
    json_data = context['response'].json()
    
    assert json_data.get('nome') == expected_name, (
        f"Erro: O nome foi alterado. Esperado: '{expected_name}', Recebido: '{json_data.get('nome')}'")