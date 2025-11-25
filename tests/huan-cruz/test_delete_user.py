import requests
from pytest_bdd import scenario, when, then

# CORREÇÃO: Aponta para o arquivo Gherkin correto
@scenario("features/TCs-Huan-Cruz.feature", "Deletar um usuário existente com sucesso")
def test_run():
    pass

@when('removo o usuário criado anteriormente')
def delete_user(context):
    id_user = context["id_usuario"]
    url = f"{context['base_url']}{context['endpoint']}/{id_user}"
    context["response"] = requests.delete(url)

@then('o sistema deve retornar status 204')
def status_204(context):
    # Aceita 200 (OK) ou 204 (No Content) para DELETE
    assert context["response"].status_code in (200, 204)

@then('ao pesquisar pelo ID removido o sistema deve retornar 404')
def ensure_deleted(context):
    id_user = context["id_usuario"]
    url = f"{context['base_url']}{context['endpoint']}/{id_user}"
    r = requests.get(url)
    assert r.status_code == 404