import requests
from pytest_bdd import scenario, when, then, parsers

@scenario('seguidores.feature', '5 - Tentar Deixar de Seguir uma Relação Inexistente (404)')
def test_deixar_de_seguir_inexistente():
    """Testa a tentativa de remover uma relação inexistente (DELETE 404)."""
    pass

@when(parsers.parse('que o usuario "{seguidor_id}" nao segue o usuario "{seguido_id}"'), target_fixture='context')
def setup_relacao_inexistente(context, seguidor_id, seguido_id):
    """Setup: Garante que a relação de seguir NÃO existe."""
    full_url = f'{context["base_url"]}{context["endpoint"]}?seguidor_id={seguidor_id}&seguido_id={seguido_id}'
    response = requests.delete(full_url)
    
    if response.status_code not in [200, 204, 404]:
        raise AssertionError(f"Falha no setup: Esperado 200/204 (deletado) ou 404 (já ausente), mas retornou {response.status_code}")
    
    return context