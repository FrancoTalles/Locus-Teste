import requests
from pytest_bdd import scenario, given, when, then, parsers

@scenario('features/posts.feature', 'Listar todos os Posts Cadastrados')
def test_run():
    pass

@when(parsers.parse('envio uma requisição GET para /post'))
def send_get_request(context):
    full_url = f"{context['base_url']}{context['endpoint']}"
    context['response'] = requests.get(full_url)
    print(context['response'].json())

@then(parsers.parse('o sistema deve retornar status 200'))
def check_status_200(context):
    assert context['response'].status_code == 200

@then(parsers.parse('deve retornar uma lista de posts'))
def check_response_is_list(context):
    json_data = context['response'].json()
    assert isinstance(json_data, list)

@then(parsers.parse('cada post deve conter os campos "{campos_string}"'))
def check_posts_schema(context, campos_string):
    json_data = context['response'].json()
    
    campos_esperados = {campo.strip().replace('"', '') for campo in campos_string.split(',')}

    for post in json_data:
        chaves_recebidas = set(post.keys())
        assert chaves_recebidas == campos_esperados, f"Esperado: {campos_esperados}, Recebido: {chaves_recebidas}"