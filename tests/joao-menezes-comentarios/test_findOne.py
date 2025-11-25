import requests
from pytest_bdd import scenario, given, when, then, parsers

@scenario('features/comentarios.feature', 'Listar um comentário ao buscar por ID')
def test_run():
    pass

@given('que tenho comentarios cadastrados no sistema')
def set_endpoint(context):
    context['endpoint'] = "/comentarios"

@when(parsers.parse('pesquiso pelo comentário com ID {id_comentario}'))
def get_comentario_by_id(context, id_comentario):
    full_url = f"{context['base_url']}{context['endpoint']}/{id_comentario}"
    context['response'] = requests.get(full_url)
    print(context['response'].json())

@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a {valor:d}'))
def check_field_int_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor