import requests
from pytest_bdd import scenario, when, then

@scenario('features/posts.feature', 'Deletar um post existente com sucesso')
def test_run():
    pass

@when('removo o post criado anteriormente')
def delete_dynamic_post(context):
    id_post = context['id_post_criado']

    print(id_post)
    
    full_url = f"{context['base_url']}{context['endpoint']}/{id_post}"
    
    context['response'] = requests.delete(full_url)

@then('o sistema deve retornar status 200')
def check_status_201(context):
    assert context['response'].status_code == 200

@then('ao pesquisar pelo ID removido o sistema deve retornar 404')
def verify_item_deleted(context):
    id_post = context['id_post_criado']
    full_url = f"{context['base_url']}{context['endpoint']}/{id_post}"
    
    response = requests.get(full_url)
    assert response.status_code == 404