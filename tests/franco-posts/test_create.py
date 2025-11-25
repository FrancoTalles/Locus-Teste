import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/posts.feature', 'Criar um novo post com sucesso')
def test_run():
    pass

@when(parsers.parse('envio um novo post com descricao "{descricao}", usuario {usuario_id:d} e local {local_id:d}'))
def send_post_request(context, descricao, usuario_id, local_id):
    full_url = f"{context['base_url']}{context['endpoint']}"
    
    payload = {
        "descricao": descricao,
        "usuario_id": usuario_id,
        "local_id": local_id,
        "imagem": ""
    }
    
    context['response'] = requests.post(full_url, json=payload)

    novo_id = context['response'].json().get('post_id')
    context['ids_para_limpeza'].append(novo_id)
    
    print(context['response'].json())

@then('o sistema deve retornar status 201')
def check_status_201(context):
    assert context['response'].status_code == 201

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field_str_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor

@then(parsers.parse('o campo "{campo}" deve ser igual a {valor:d}'))
def check_field_int_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor