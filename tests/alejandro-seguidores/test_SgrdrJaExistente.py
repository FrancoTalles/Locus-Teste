import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('seguidores.feature', '4 - Tentar Seguir um Usuário que Já é Seguido (Conflito 409)')
def test_seguir_conflito():
    """Testa a tentativa de seguir um usuário que já é seguido (POST 409)."""
    pass

@when(parsers.parse('que o usuario "{seguidor_id}" já segue o usuario "{seguido_id}"'), target_fixture='context')
def setup_seguir_ja_existente(context, seguidor_id, seguido_id):
    """Garante que a relação de seguir já existe antes de tentar seguir de novo."""
    full_url = f'{context["base_url"]}{context["endpoint"]}'
    payload = {"seguidor_id": int(seguidor_id), "seguido_id": int(seguido_id)}
    
    response = requests.post(full_url, json=payload)
    
    if response.status_code not in [201, 409]:
         raise AssertionError(f"Falha no setup: Esperado 201 ou 409, mas retornou {response.status_code}")
    
    return context