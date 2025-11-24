Feature: Crud de Local - Victor Hugo 
    Como usuário da API
    Quero realizar operações de CRUD no recurso de Local

    Background:
        Given que a url base da API é "http://localhost:3000"
        And que o endpoint de local é "/local"


    Scenario: Listar todos os Locais Cadastrados
        Given que tenho locais cadastrados no sistema
        When envio uma requisição GET para /local
        Then o sistema deve retornar status 200
        And deve retornar uma lista de locais


    Scenario: Criar um novo Local
        Given que possuo dados válidos para criar um local
        When envio uma requisição POST para /local com esses dados
        Then o sistema deve retornar status 201
        And deve retornar o objeto do local criado contendo local_id


    Scenario: Buscar um Local por ID existente
        Given que possuo o ID de um local existente
        When envio uma requisição GET para /local/{id}
        Then o sistema deve retornar status 200
        And deve retornar os dados completos do local correspondente


    Scenario: Buscar um Local por ID inexistente
        Given que possuo um ID inexistente
        When envio uma requisição GET para /local/{id}
        Then o sistema deve retornar status 404
        And deve retornar a mensagem "Local com ID {id} não encontrado."


    Scenario: Atualizar um Local existente
        Given que possuo o ID de um local existente e novos dados válidos
        When envio uma requisição PATCH para /local/{id} com esses dados
        Then o sistema deve retornar status 200
        And deve retornar o local atualizado


    Scenario: Atualizar um Local inexistente
        Given que possuo um ID inexistente
        When envio uma requisição PATCH para /local/{id}
        Then o sistema deve retornar status 404


    Scenario: Remover um Local existente
        Given que possuo o ID de um local existente
        When envio uma requisição DELETE para /local/{id}
        Then o sistema deve retornar status 204


    Scenario: Remover um Local inexistente
        Given que possuo um ID inexistente
        When envio uma requisição DELETE para /local/{id}
        Then o sistema deve retornar status 404
