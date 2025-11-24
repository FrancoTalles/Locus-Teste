import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/posts.feature', 'Atualizar um post existente com sucesso')
def test_run():
    pass

@when(parsers.parse('atualizo o post criado anteriormente com a nova descricao "{nova_desc}"'))
def update_dynamic_post(context, nova_desc):
    id_post = context['id_post_criado']
    
    full_url = f"{context['base_url']}{context['endpoint']}/{id_post}"
    
    payload = {
        "descricao": nova_desc,
    }
    
    context['response'] = requests.patch(full_url, json=payload)
    print(context['response'].json())

@then('o sistema deve retornar status 200')
def check_status_201(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field_str_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor