Feature: Crud de Posts - Franco
    Como usuário da API
    Quero realizar operações de CRUD no recurso de Posts

    Background:
        Given que a url base da API é "http://localhost:3000"
        And que o endpoint de posts é "/post" 

    Scenario: Listar todos os Posts Cadastrados
        Given que tenho posts cadastrados no sistema
        When envio uma requisição GET para /post
        Then o sistema deve retornar status 200
        And deve retornar uma lista de posts