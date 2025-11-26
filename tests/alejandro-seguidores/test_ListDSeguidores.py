import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('seguidores.feature', '2 - Deixar de Seguir um Usuário com Sucesso')
def test_deixar_de_seguir_sucesso():
    """Testa a remoção de uma relação de seguidor com sucesso (DELETE 200)."""
    pass

@when(parsers.parse('eu envio uma requisição DELETE para "/seguidores" com usuario "{seguidor_id}" deixando de seguir "{seguido_id}"'), target_fixture='context')
def send_delete_request_deixar_de_seguir(context, seguidor_id, seguido_id):
    full_url = f'{context["base_url"]}{context["endpoint"]}?seguidor_id={seguidor_id}&seguido_id={seguido_id}'
    
    context['response'] = requests.delete(full_url) 
    print(f"DELETE Status Code: {context['response'].status_code}")
    return context

@then(parsers.parse('ao tentar buscar o seguidor "{seguidor_id}" seguindo "{seguido_id}" o sistema deve retornar 404'))
def verify_relacao_deletada(context, seguidor_id, seguido_id):
    """Verifica que a relação foi de fato deletada (GET deve retornar 404)."""
    full_url = f'{context["base_url"]}{context["endpoint"]}?seguidor_id={seguidor_id}&seguido_id={seguido_id}'
    response = requests.get(full_url)
    
    assert response.status_code == 404, f"Esperado 404 após DELETE, mas retornou {response.status_code}"

@when(parsers.parse('que eu sigo o usuario "{seguido_id}" com o meu usuario "{seguidor_id}"'), target_fixture='context')
def setup_relacao_existente(context, seguidor_id, seguido_id):
    """Setup: Garante que a relação de seguir existe."""
    full_url = f'{context["base_url"]}{context["endpoint"]}'
    payload = {"seguidor_id": int(seguidor_id), "seguido_id": int(seguido_id)}
    response = requests.post(full_url, json=payload)
    
    if response.status_code not in [201, 409]:
         raise AssertionError(f"Falha no setup: Esperado 201 (criado) ou 409 (já existe), mas retornou {response.status_code}")
    return context