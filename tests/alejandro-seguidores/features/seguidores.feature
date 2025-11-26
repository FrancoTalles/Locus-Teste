Feature: CRUD de Seguidores - David Acosta
    Como usuário da API
    Quero realizar operações de CRUD no recurso de Posts

  Background:
    Given que a url base da API é "http://72.61.43.201"
    And que o endpoint de seguidores é "/seguidores"

  Scenario: Seguir um Usuário com Sucesso
    Given que eu tenho 2 usuarios cadastrados no sistema
    When eu envio uma requisição POST para "/seguidores" com usuario "2" seguindo usuario "3"
    Then o sistema deve retornar status 201
    And o campo "seguidor_id" deve ser igual a "2"
    And o campo "seguido_id" deve ser igual a "3"

  Scenario: Deixar de Seguir um Usuário com Sucesso
    Given que eu sigo o usuario "3" com o meu usuario "2"
    When eu envio uma requisição DELETE para "/seguidores" com usuario "2" deixando de seguir "3"
    Then o sistema deve retornar status 200
    And ao tentar buscar o seguidor "2" seguindo "3" o sistema deve retornar 404

  Scenario: Listar Usuários Seguidos por um Usuário
    Given que o usuario "3" segue os usuarios "1" e "2"
    When eu envio uma requisição GET para "/seguidores" do usuario "3"
    Then o sistema deve retornar status 200
    And o retorno deve ser uma lista de 2 seguidos
    And o campo "seguido_id" deve conter "1" e "2"

  Scenario: Tentar Seguir um Usuário que Já é Seguido (Conflito 409)
    Given que o usuario "2" já segue o usuario "3"
    When eu envio uma requisição POST para "/seguidores" com usuario "2" seguindo usuario "3"
    Then o sistema deve retornar status 409

  Scenario: Tentar Deixar de Seguir uma Relação Inexistente (404)
    Given que o usuario "2" nao segue o usuario "9999"
    When eu envio uma requisição DELETE para "/seguidores" com usuario "2" deixando de seguir "9999"
    Then o sistema deve retornar status 404