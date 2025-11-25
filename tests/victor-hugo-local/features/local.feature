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


    # --- Cenário de (POST) ---

    Scenario: Criar um novo Local com sucesso
    When envio um novo local com nome "Praia do Futuro", endereco "Av. Zezinho", categoria "Praia", latitude "-3.7554", longitude "-38.4897"
    Then o sistema deve retornar status "201"
    And o campo "nome" deve ser igual a "Praia do Futuro"
    And o campo "categoria" deve ser igual a "Praia"
    And o campo "local_id" deve ser preenchido (não nulo)

    # --- Cenários de (PATCH) ---

    Scenario: Atualizar um Local existente com sucesso
    Given que tenho locais cadastrados no sistema
    When atualizo o local criado anteriormente com a nova categoria "Restaurante"
    Then o sistema deve retornar status 200
    And o campo "categoria" deve ser igual a "Restaurante"
    And o campo "nome" deve permanecer o original

    # --- Cenários de (DELETE) ---

    Scenario: Deletar um Local existente com sucesso
    Given que tenho locais cadastrados no sistema
    When removo o local criado anteriormente
    Then o sistema deve retornar status 204
    # Confirmação da remoção
    And ao pesquisar pelo ID removido o sistema deve retornar 404

