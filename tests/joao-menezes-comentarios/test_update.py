import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/comentarios.feature', 'Atualizar um comentario existente')
def test_run():
    pass

@when(parsers.parse('atualizo o comentário criado anteriormente com o novo texto "{novo_comentario}"'))
def update_dynamic_comentario(context, novo_comentario):
    id_comentario = context['id_comentario_criado']
    
    full_url = f"{context['base_url']}{context['endpoint']}/{id_comentario}"
    
    payload = {
        "comentario": novo_comentario,
    }
    
    context['response'] = requests.patch(full_url, json=payload)
    print(context['response'].json())

@then('o sistema deve retornar status 200')
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field_str_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor