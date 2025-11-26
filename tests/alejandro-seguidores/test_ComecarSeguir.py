import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('seguidores.feature', '1 - Seguir um Usuário com Sucesso')
def test_seguir_sucesso():
    """Testa a criação de uma relação de seguidor com sucesso (POST 201)."""
    pass

@when(parsers.parse('eu envio uma requisição POST para "/seguidores" com usuario "{seguidor_id}" seguindo usuario "{seguido_id}"'), target_fixture='context')
def send_post_request_seguir(context, seguidor_id, seguido_id):
    full_url = f'{context["base_url"]}{context["endpoint"]}' 
    
    payload = {
        "seguidor_id": int(seguidor_id),
        "seguido_id": int(seguido_id)
    }
    
    context['response'] = requests.post(full_url, json=payload)
    print(f"POST Response: {context['response'].json()}")
    return context 