import pytest
import requests
from pytest_bdd import given, parsers

@pytest.fixture
def context():
    return {
        'ids_para_limpeza': []
    }

@given(parsers.parse('que a url base da API é "{url}"'))
def set_base_url(context, url):
    context['base_url'] = url

@given(parsers.parse('que o endpoint de posts é "{endpoint}"'))
def set_endpoint(context, endpoint):
    context['endpoint'] = endpoint