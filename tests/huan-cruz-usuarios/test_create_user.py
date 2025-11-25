import requests
from pytest_bdd import scenario, when, then, parsers

@scenario("features/TCs-Huan-Cruz.feature", "Criar um novo usuário com sucesso")
def test_run():
    pass

@when(parsers.parse('envio um novo usuário com nome "{nome}", email "{email}" e senha "{senha}"'))
def send_create_user(context, nome, email, senha):
    url = f"{context['base_url']}{context['endpoint']}"
    payload = {
        "nome": nome,
        "email": email,
        "senha_hash": senha,
        "foto_perfil": ""
    }
    context["response"] = requests.post(url, json=payload)

    novo_id = context['response'].json().get('post_id')
    context['ids_para_limpeza'].append(novo_id)

@then('o sistema deve retornar status 201')
def check_status(context):
    assert context["response"].status_code == 201

@then(parsers.parse('o campo "{campo}" deve ser igual a "{valor}"'))
def check_field(context, campo, valor):
    # O valor é uma string no .feature, então não precisa de conversão
    assert context["response"].json()[campo] == valor