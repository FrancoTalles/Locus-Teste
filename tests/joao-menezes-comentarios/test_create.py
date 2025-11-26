import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('features/comentarios.feature', 'Criar um novo comentario')
def test_run():
    pass

@when(parsers.parse('envio um novo comentario "{comentario}" do usuario {usuario_id:d} no post {post_id:d}'))
def send_comentario_request(context, comentario, usuario_id, post_id):
    full_url = f"{context['base_url']}/comentarios"
        
    payload = {
        "comentario": comentario,
        "usuario_id": usuario_id,
        "post_id": post_id
    }

    context['response'] = requests.post(full_url, json=payload)

    novo_id = context['response'].json().get('comentario_id')
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