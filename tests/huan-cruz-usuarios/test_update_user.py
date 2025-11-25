import requests
from pytest_bdd import scenario, when, then, parsers

# CORREÇÃO: Aponta para o arquivo Gherkin correto
@scenario("features/TCs-Huan-Cruz.feature", "Atualizar um usuário existente com sucesso")
def test_run():
    pass

@when(parsers.parse('atualizo o usuário criado anteriormente com o novo nome "{novo_nome}"'))
def update_user(context, novo_nome):
    id_user = context["id_usuario"]
    url = f"{context['base_url']}{context['endpoint']}/{id_user}"
    # O payload deve ser um objeto JSON
    context["response"] = requests.patch(url, json={"nome": novo_nome})

@then('o sistema deve retornar status 200')
def status_200(context):
    assert context["response"].status_code == 200

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field(context, campo, valor):
    assert context["response"].json()[campo] == valor