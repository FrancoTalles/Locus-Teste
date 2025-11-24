import requests
from pytest_bdd import scenario, given, when, then, parsers

@scenario('features/posts.feature', 'Listar um post ao buscar por ID')
def test_run():
    pass

@when(parsers.parse('pesquiso pelo post com ID {id_post}'))
def get_post_by_id(context, id_post):
    full_url = f"{context['base_url']}{context['endpoint']}/{id_post}"
    context['response'] = requests.get(full_url)
    print(context['response'].json())

@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a {valor:d}'))
def check_field_int_value(context, campo, valor):
    json_data = context['response'].json()
    assert json_data[campo] == valor
