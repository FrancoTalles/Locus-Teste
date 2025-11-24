import pytest
import requests
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('features/local.feature')

@pytest.fixture
def context():
    return {}

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de local é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint

@when('envio uma requisição GET para /local')
def send_get_request(context):
    full_url = f"{context['base_url']}{context['endpoint']}"
    context['response'] = requests.get(full_url)

@then('o sistema deve retornar status 200')
def check_status_200(context):
    assert context['response'].status_code == 200

@then('deve retornar uma lista de locais')
def check_response_is_list(context):
    json_data = context['response'].json()
    assert isinstance(json_data, list)