import requests
from pytest_bdd import scenario, when, then

@scenario('features/local.feature', 'Deletar um Local existente com sucesso')
def test_run():
    pass

@when('removo o local criado anteriormente')
def delete_dynamic_post(context):
    local_id = context['id_local_criado']

    print(local_id)
    
    full_url = f"{context['base_url']}{context['endpoint']}/{local_id}"
    
    context['response'] = requests.delete(full_url)

@then('o sistema deve retornar status 204')
def check_status_204(context):
    assert context['response'].status_code == 204

@then('ao pesquisar pelo ID removido o sistema deve retornar 404')
def verify_item_deleted(context):
    local_id = context['id_local_criado']
    full_url = f"{context['base_url']}{context['endpoint']}/{local_id}"
    
    response = requests.get(full_url)
    assert response.status_code == 404