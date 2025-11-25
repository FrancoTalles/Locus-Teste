Feature: CRUD de Usuários - Huan Cruz
  Como usuário da API
  Quero realizar operações de CRUD no recurso de Usuários

  Background:
    Given que a url base da API é "http://72.61.43.201"
    And que o endpoint de usuarios é "/usuarios"

  Scenario: Listar todos os Usuários Cadastrados
    Given que tenho usuários cadastrados no sistema
    When envio uma requisição GET para /usuarios
    Then o sistema deve retornar status 200
    And deve retornar uma lista de usuários

  Scenario: Listar um usuário ao buscar por ID
    Given que tenho usuários cadastrados no sistema
    When pesquiso pelo usuário com ID 2
    Then o sistema deve retornar status 200
    And o campo "usuario_id" deve ser igual a 2

  Scenario: Criar um novo usuário com sucesso
    When envio um novo usuário com nome "Usuario Teste", email "usuario.teste@example.com" e senha "123456"
    Then o sistema deve retornar status 201
    And o campo "nome" deve ser igual a "Usuario Teste"

  Scenario: Atualizar um usuário existente com sucesso
    Given que tenho usuários cadastrados no sistema
    When atualizo o usuário criado anteriormente com o novo nome "Nome Atualizado"
    Then o sistema deve retornar status 200
    And o campo "nome" deve ser igual a "Nome Atualizado"

  Scenario: Deletar um usuário existente com sucesso
    Given que tenho usuários cadastrados no sistema
    When removo o usuário criado anteriormente
    Then o sistema deve retornar status 204
    And ao pesquisar pelo ID removido o sistema deve retornar 404
