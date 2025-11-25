import requests
from pytest_bdd import scenario, when, then, parsers

# CORREÇÃO: Aponta para o arquivo Gherkin correto
@scenario("features/TCs-Huan-Cruz.feature", "Listar um usuário ao buscar por ID")
def test_run():
    pass

@when(parsers.parse("pesquiso pelo usuário com ID {id_user}"))
def get_by_id(context, id_user):
 
    url = f"{context['base_url']}{context['endpoint']}/{id_user}"
    context["response"] = requests.get(url)
    
@then('o sistema deve retornar status 200')
def status_200(context):
    assert context["response"].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a 2'))
def validate_field(context, campo):
 
    assert context["response"].json().get(campo) == 2