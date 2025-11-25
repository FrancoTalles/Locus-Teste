import requests
from pytest_bdd import scenario, when, then

# CORREÇÃO: Aponta para o arquivo Gherkin correto
@scenario("features/TCs-Huan-Cruz.feature", "Listar todos os Usuários Cadastrados")
def test_run():
    pass

@when('envio uma requisição GET para /usuarios')
def get_all(context):
    url = f"{context['base_url']}{context['endpoint']}"
    context['response'] = requests.get(url)
    
@then('o sistema deve retornar status 200')
def status_200(context):
    assert context["response"].status_code == 200

@then('deve retornar uma lista de usuários')
def is_list(context):
    assert isinstance(context["response"].json(), list)