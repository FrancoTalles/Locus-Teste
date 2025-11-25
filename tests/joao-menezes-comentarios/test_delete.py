import requests
from pytest_bdd import scenario, when, then

@scenario('features/comentarios.feature', 'Deletar um comentário existente')
def test_run():
    pass

@when('removo o comentário criado anteriormente')
def delete_dynamic_comentario(context):
    id_comentario = context['id_comentario_criado']

    print(id_comentario)
    
    full_url = f"{context['base_url']}{context['endpoint']}/{id_comentario}"
    
    context['response'] = requests.delete(full_url)

@then('o sistema deve retornar status 200')
def check_status_200(context):
    assert context['response'].status_code == 200

@then('ao pesquisar pelo ID removido o sistema deve retornar 404')
def verify_item_deleted(context):
    id_comentario = context['id_comentario_criado']
    full_url = f"{context['base_url']}{context['endpoint']}/{id_comentario}"
    
    response = requests.get(full_url)
    assert response.status_code == 404