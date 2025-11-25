Feature: Crud de Locais - Victor Hugo
  Como usuário da API
  Quero realizar operações CRUD no recurso de Local
  Para gerenciar e consultar informações de diferentes lugares.

  Background:
    Given que a url base da API é "http://localhost:3000"
    And que o endpoint de local é "/local"


    # --- Cenários de (GET) ---

    Scenario: Listar todos os Locais Cadastrados
    Given que tenho locais cadastrados no sistema
    When envio uma requisição GET para /local
    Then o sistema deve retornar status 200
    And deve retornar uma lista de locais
    # Validação dos campos da entidade Local
    And cada local deve conter os campos "local_id", "nome", "endereco", "categoria", "latitude", "longitude", "created_at"

    Scenario: Listar um Local ao buscar por ID
    Given que tenho locais cadastrados no sistema
    When pesquiso pelo local com ID 1
    Then o sistema deve retornar status 200
    And o campo "local_id" deve ser igual a 1
    # Adiciona uma validação de dado específico
    And o campo "nome" do local deve ser "Largo Sao Sebastiao"
